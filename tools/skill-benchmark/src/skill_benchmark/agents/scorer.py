"""Score one generated output against the benchmark rubric.

The scorer evaluates a single output in isolation (no side-by-side comparison)
on four dimensions: coverage, specificity, correctness, and completeness.
It returns a structured :class:`~skill_benchmark.models.ScoringResult` parsed
from model JSON, with one retry when the response is invalid.

Deliverable: repeatable 1–5 dimension scores and rationales for baseline and
with-skill runs. Used by :class:`~skill_benchmark.runner.BenchmarkRunner`.
"""

from __future__ import annotations

import json
import re

from skill_benchmark.config import BenchmarkConfig
from skill_benchmark.models import DimensionScore, ScoringResult, TaskPrompt
from skill_benchmark.provider import LLMProvider

_SCORER_SYSTEM = """You evaluate software-engineering task output on four dimensions.
Score each dimension from 1 to 5 (integers only).

Dimensions:
- coverage: Did the output address all required sub-tasks?
- specificity: Are commands, formats, and values concrete (not vague)?
- correctness: Is the output factually and technically correct?
- completeness: Could an engineer act on this output without further clarification?

Return ONLY valid JSON with this shape:
{
  "coverage": {"score": 1, "rationale": "..."},
  "specificity": {"score": 1, "rationale": "..."},
  "correctness": {"score": 1, "rationale": "..."},
  "completeness": {"score": 1, "rationale": "..."}
}
"""


class ScorerAgent:
    """Score one generated output independently."""

    def __init__(self, config: BenchmarkConfig, client=None) -> None:
        """Create a scorer using the scorer model configuration.

        Args:
            config (BenchmarkConfig): Benchmark settings including scorer URL/model.
            client: Optional injected client for tests.
        """

        scorer_config = config.model_copy(
            update={
                "llm_base_url": config.scorer_base_url,
                "llm_model": config.scorer_model,
            }
        )
        self._provider = LLMProvider(scorer_config, client=client)

    async def score(self, task: TaskPrompt, output: str) -> ScoringResult:
        """Score one output against the task rubric.

        The scorer sees only one output at a time to avoid comparison bias.

        Args:
            task (TaskPrompt): Original benchmark task.
            output (str): Generated markdown to evaluate.

        Returns:
            ScoringResult: Structured dimension scores.

        Raises:
            ValueError: If the model response cannot be parsed as valid JSON scores.
        """

        user_prompt = (
            f"Task prompt:\n{task.prompt}\n\n"
            f"Expected coverage:\n{task.expected_coverage or '(not specified)'}\n\n"
            f"Output to score:\n{output}"
        )
        messages = [
            {"role": "system", "content": _SCORER_SYSTEM},
            {"role": "user", "content": user_prompt},
        ]

        last_error: Exception | None = None
        for attempt in range(2):
            response = await self._provider.complete(messages=messages, temperature=0.0)
            try:
                return _parse_scoring_result(response.content)
            except ValueError as exc:
                last_error = exc
                if attempt == 0:
                    messages.append({"role": "assistant", "content": response.content})
                    messages.append(
                        {
                            "role": "user",
                            "content": "Your previous response was not valid JSON. "
                            "Return ONLY the JSON object with integer scores 1-5.",
                        }
                    )
        raise ValueError("Scorer returned invalid JSON after retry.") from last_error


def _parse_scoring_result(raw: str) -> ScoringResult:
    """Parse scorer JSON into a ScoringResult."""

    payload = _extract_json_object(raw)
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError("Scorer response is not valid JSON.") from exc

    return ScoringResult(
        coverage=_parse_dimension(data, "coverage"),
        specificity=_parse_dimension(data, "specificity"),
        correctness=_parse_dimension(data, "correctness"),
        completeness=_parse_dimension(data, "completeness"),
    )


def _extract_json_object(raw: str) -> str:
    """Return the first JSON object found in a model response."""

    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, flags=re.DOTALL)
    if fenced:
        return fenced.group(1)
    start = raw.find("{")
    end = raw.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found in scorer response.")
    return raw[start : end + 1]


def _parse_dimension(data: dict, key: str) -> DimensionScore:
    """Parse one dimension entry from scorer JSON."""

    entry = data.get(key)
    if not isinstance(entry, dict):
        raise ValueError(f"Missing dimension: {key}")

    score = entry.get("score")
    rationale = entry.get("rationale", "")
    if not isinstance(score, int) or score < 1 or score > 5:
        raise ValueError(f"Invalid score for {key}: {score!r}")
    if not isinstance(rationale, str):
        raise ValueError(f"Invalid rationale for {key}.")

    return DimensionScore(score=score, rationale=rationale.strip())
