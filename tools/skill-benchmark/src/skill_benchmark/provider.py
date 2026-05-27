"""OpenAI-compatible provider adapter for benchmark calls.

The benchmark framework needs a single interface for local and cloud model
endpoints. This wrapper keeps call sites stable while implementations evolve.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from openai import AsyncOpenAI

from .config import BenchmarkConfig


@dataclass(frozen=True)
class LLMResponse:
    """A parsed LLM response plus usage metadata."""

    content: str
    model: str
    input_tokens: int | None = None
    output_tokens: int | None = None


class LLMProvider:
    """Wrap an OpenAI-compatible async chat client."""

    def __init__(self, config: BenchmarkConfig, client: Any | None = None) -> None:
        """Create an LLM provider for benchmark runs.

        Args:
            config (BenchmarkConfig): Benchmark settings (base URL, model, API key).
            client (Any | None): Optional pre-constructed client for tests/mocking.
                When omitted, an `openai.AsyncOpenAI` client is created.

        Raises:
            ValueError: If `config.api_key` is empty and `client` is not provided.
        """

        if client is None and not config.api_key:
            raise ValueError("OPENAI_API_KEY must be set (or pass an explicit client).")

        self._config = config
        self._client = client or AsyncOpenAI(api_key=config.api_key, base_url=config.llm_base_url)

    async def complete(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.0,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        """Generate a completion for chat messages.

        Calls the configured OpenAI-compatible endpoint and returns the first choice
        content plus token counts when the client provides usage metadata.

        Args:
            messages (list[dict[str, str]]): Chat messages for the completion.
            temperature (float): Sampling temperature.
            max_tokens (int | None): Optional token cap for the completion.

        Returns:
            LLMResponse: Parsed content, model name, and optional token usage.

        Raises:
            RuntimeError: If the response shape does not contain a usable choice/message.
        """

        resp = await self._client.chat.completions.create(
            model=self._config.llm_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        try:
            choice = resp.choices[0]
            content = (choice.message.content or "").strip()
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError("Unexpected OpenAI response shape.") from exc

        usage = getattr(resp, "usage", None)
        input_tokens = getattr(usage, "prompt_tokens", None) if usage is not None else None
        output_tokens = getattr(usage, "completion_tokens", None) if usage is not None else None

        return LLMResponse(
            content=content,
            model=self._config.llm_model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )
