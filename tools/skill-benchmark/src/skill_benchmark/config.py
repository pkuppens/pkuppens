"""Configuration model for skill benchmark runs.

This module centralizes environment-based settings so benchmark runs are
repeatable in local and CI environments without hard-coded secrets.
"""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BenchmarkConfig(BaseSettings):
    """Load benchmark configuration from environment variables.

    Fields are designed to support OpenAI and OpenAI-compatible providers
    (for example local Ollama servers using the same API surface).
    """

    model_config = SettingsConfigDict(extra="ignore", env_file=None)

    api_key: str = Field(default="", validation_alias="OPENAI_API_KEY")

    llm_base_url: str = Field(
        default="https://api.openai.com/v1",
        validation_alias="BENCHMARK_LLM_BASE_URL",
    )
    llm_model: str = Field(default="gpt-4o-mini", validation_alias="BENCHMARK_LLM_MODEL")

    scorer_base_url: str = Field(
        default="https://api.openai.com/v1",
        validation_alias="BENCHMARK_SCORER_BASE_URL",
    )
    scorer_model: str = Field(
        default="gpt-4o-mini",
        validation_alias="BENCHMARK_SCORER_MODEL",
    )

    tmp_dir: Path = Field(
        default=Path("tmp/skills/benchmark"),
        validation_alias="BENCHMARK_TMP_DIR",
    )
    docs_dir: Path = Field(
        default=Path("docs/skills/benchmark"),
        validation_alias="BENCHMARK_DOCS_DIR",
    )
