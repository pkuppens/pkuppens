import pytest

from skill_benchmark.agents.generator import GeneratorAgent
from skill_benchmark.config import BenchmarkConfig
from skill_benchmark.models import SkillContent, TaskPrompt
from skill_benchmark.provider import LLMProvider


class _RecordingCompletions:
    def __init__(self) -> None:
        self.calls: list[list[dict[str, str]]] = []

    async def create(self, *, model, messages, temperature, max_tokens):
        self.calls.append(messages)

        class _Resp:
            choices = [type("C", (), {"message": type("M", (), {"content": "generated"})()})()]
            usage = None

        return _Resp()


class _RecordingClient:
    def __init__(self) -> None:
        self.chat = type("Chat", (), {"completions": _RecordingCompletions()})()


@pytest.mark.asyncio
async def test_generator_baseline_uses_prompt_only_system(monkeypatch: pytest.MonkeyPatch) -> None:
    """Baseline generation should not include skill content."""

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    client = _RecordingClient()
    provider = LLMProvider(BenchmarkConfig(_env_file=None), client=client)
    agent = GeneratorAgent(provider)

    task = TaskPrompt(name="t", prompt="Do the task", expected_coverage="")
    result = await agent.generate(task, skill=None)

    assert result.output == "generated"
    system = client.chat.completions.calls[0][0]["content"]
    assert "skill reference" not in system.lower()


@pytest.mark.asyncio
async def test_generator_with_skill_injects_content(monkeypatch: pytest.MonkeyPatch) -> None:
    """With-skill generation should include skill markdown in the system prompt."""

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    client = _RecordingClient()
    provider = LLMProvider(BenchmarkConfig(_env_file=None), client=client)
    agent = GeneratorAgent(provider)

    task = TaskPrompt(name="t", prompt="Do the task", expected_coverage="")
    skill = SkillContent(name="issue-workflow", content="SKILL BODY")
    await agent.generate(task, skill=skill)

    system = client.chat.completions.calls[0][0]["content"]
    assert "SKILL BODY" in system


@pytest.mark.asyncio
async def test_generator_runs_use_separate_message_lists(monkeypatch: pytest.MonkeyPatch) -> None:
    """Baseline and with-skill calls must not share message history."""

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    client = _RecordingClient()
    provider = LLMProvider(BenchmarkConfig(_env_file=None), client=client)
    agent = GeneratorAgent(provider)
    task = TaskPrompt(name="t", prompt="Do the task", expected_coverage="")
    skill = SkillContent(name="s", content="SKILL")

    await agent.generate(task, skill=None)
    await agent.generate(task, skill=skill)

    assert len(client.chat.completions.calls) == 2
    assert client.chat.completions.calls[0] is not client.chat.completions.calls[1]
