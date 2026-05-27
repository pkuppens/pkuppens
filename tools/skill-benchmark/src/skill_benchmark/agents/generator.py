"""Generator agent for baseline and with-skill benchmark runs."""

from __future__ import annotations

from skill_benchmark.models import GenerationResult, SkillContent, TaskPrompt
from skill_benchmark.provider import LLMProvider

_BASELINE_SYSTEM = (
    "You are a software engineer. Create a GitHub issue based on the following task. "
    "Return only the issue body in markdown."
)

_WITH_SKILL_SYSTEM = (
    "You are a software engineer. Create a GitHub issue based on the following task. "
    "Use the skill reference material below to improve structure and quality. "
    "Return only the issue body in markdown.\n\n"
    "--- Skill reference ---\n{skill_content}"
)


class GeneratorAgent:
    """Generate benchmark outputs with and without skill context."""

    def __init__(self, provider: LLMProvider) -> None:
        """Create a generator backed by an LLM provider.

        Args:
            provider (LLMProvider): OpenAI-compatible provider for generation calls.
        """

        self._provider = provider

    async def generate(
        self,
        task: TaskPrompt,
        skill: SkillContent | None = None,
    ) -> GenerationResult:
        """Generate output for one task, optionally with skill context.

        Baseline and with-skill runs use separate message lists so context does not
        leak between them.

        Args:
            task (TaskPrompt): Benchmark task prompt.
            skill (SkillContent | None): Skill markdown to inject into the system
                prompt. When ``None``, run baseline (prompt only).

        Returns:
            GenerationResult: Generated markdown and token usage metadata.
        """

        if skill is None:
            system_prompt = _BASELINE_SYSTEM
        else:
            system_prompt = _WITH_SKILL_SYSTEM.format(skill_content=skill.content)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": task.prompt},
        ]
        response = await self._provider.complete(messages=messages, temperature=0.0)
        return GenerationResult(
            output=response.content,
            model=response.model,
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
        )
