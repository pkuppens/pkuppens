import pytest

from skill_benchmark.config import BenchmarkConfig
from skill_benchmark.provider import LLMProvider


class _StubUsage:
    def __init__(self) -> None:
        self.prompt_tokens = 3
        self.completion_tokens = 5


class _StubMessage:
    def __init__(self, content: str) -> None:
        self.content = content


class _StubChoice:
    def __init__(self, content: str) -> None:
        self.message = _StubMessage(content=content)


class _StubResponse:
    def __init__(self, content: str) -> None:
        self.choices = [_StubChoice(content=content)]
        self.usage = _StubUsage()


class _StubCompletions:
    async def create(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        temperature: float,
        max_tokens: int | None,
    ):
        assert messages == [{"role": "user", "content": "hi"}]
        assert temperature == 0.0
        assert model == "gpt-4o-mini"
        assert max_tokens == 10
        return _StubResponse(content="hello from llm")


class _StubChat:
    def __init__(self) -> None:
        self.completions = _StubCompletions()


class _StubClient:
    def __init__(self) -> None:
        self.chat = _StubChat()


def test_provider_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    """Provider init should require an API key when no client is injected."""

    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    cfg = BenchmarkConfig()

    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        LLMProvider(cfg, client=None)


@pytest.mark.asyncio
async def test_provider_complete_parses_response(monkeypatch: pytest.MonkeyPatch) -> None:
    """Provider.complete should parse the first choice and usage tokens."""

    monkeypatch.setenv("OPENAI_API_KEY", "test-api-key")
    cfg = BenchmarkConfig()

    provider = LLMProvider(cfg, client=_StubClient())
    resp = await provider.complete(
        messages=[{"role": "user", "content": "hi"}],
        temperature=0.0,
        max_tokens=10,
    )

    assert resp.content == "hello from llm"
    assert resp.model == cfg.llm_model
    assert resp.input_tokens == 3
    assert resp.output_tokens == 5
