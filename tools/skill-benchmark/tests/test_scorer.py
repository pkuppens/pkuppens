import json

import pytest

from skill_benchmark.agents.scorer import ScorerAgent, _parse_scoring_result
from skill_benchmark.config import BenchmarkConfig
from skill_benchmark.models import TaskPrompt


class _ScorerCompletions:
    def __init__(self, payloads: list[str]) -> None:
        self._payloads = payloads
        self.calls = 0

    async def create(self, *, model, messages, temperature, max_tokens):
        content = self._payloads[min(self.calls, len(self._payloads) - 1)]
        self.calls += 1

        class _Resp:
            choices = [type("C", (), {"message": type("M", (), {"content": content})()})()]
            usage = None

        return _Resp()


class _ScorerClient:
    def __init__(self, payloads: list[str]) -> None:
        self.chat = type("Chat", (), {"completions": _ScorerCompletions(payloads)})()


def test_parse_scoring_result_accepts_fenced_json() -> None:
    """Parser should read JSON wrapped in markdown fences."""

    raw = """```json
{
  "coverage": {"score": 3, "rationale": "ok"},
  "specificity": {"score": 4, "rationale": "good"},
  "correctness": {"score": 5, "rationale": "fine"},
  "completeness": {"score": 2, "rationale": "partial"}
}
```"""
    result = _parse_scoring_result(raw)
    assert result.total == 14
    assert result.coverage.score == 3


def test_parse_scoring_result_rejects_invalid_score() -> None:
    """Invalid dimension scores should raise ValueError."""

    raw = json.dumps(
        {
            "coverage": {"score": 6, "rationale": "too high"},
            "specificity": {"score": 3, "rationale": "ok"},
            "correctness": {"score": 3, "rationale": "ok"},
            "completeness": {"score": 3, "rationale": "ok"},
        }
    )
    with pytest.raises(ValueError, match="Invalid score"):
        _parse_scoring_result(raw)


@pytest.mark.asyncio
async def test_scorer_retries_on_invalid_json(monkeypatch: pytest.MonkeyPatch) -> None:
    """Scorer should retry once when the model returns malformed JSON."""

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    valid = json.dumps(
        {
            "coverage": {"score": 2, "rationale": "a"},
            "specificity": {"score": 3, "rationale": "b"},
            "correctness": {"score": 4, "rationale": "c"},
            "completeness": {"score": 5, "rationale": "d"},
        }
    )
    client = _ScorerClient(["not json", valid])
    agent = ScorerAgent(BenchmarkConfig(_env_file=None), client=client)
    task = TaskPrompt(name="t", prompt="prompt", expected_coverage="coverage")

    result = await agent.score(task, "output")
    assert result.total == 14
    assert client.chat.completions.calls == 2
