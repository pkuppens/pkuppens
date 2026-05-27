from pathlib import Path

import pytest

from skill_benchmark.config import BenchmarkConfig


def test_config_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    """Defaults should be stable when no environment variables are set."""

    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("BENCHMARK_LLM_BASE_URL", raising=False)
    monkeypatch.delenv("BENCHMARK_LLM_MODEL", raising=False)
    monkeypatch.delenv("BENCHMARK_SCORER_BASE_URL", raising=False)
    monkeypatch.delenv("BENCHMARK_SCORER_MODEL", raising=False)
    monkeypatch.delenv("BENCHMARK_TMP_DIR", raising=False)
    monkeypatch.delenv("BENCHMARK_DOCS_DIR", raising=False)

    cfg = BenchmarkConfig(_env_file=None)

    assert cfg.api_key == ""
    assert cfg.llm_base_url == "https://api.openai.com/v1"
    assert cfg.llm_model == "gpt-4o-mini"
    assert cfg.scorer_base_url == "https://api.openai.com/v1"
    assert cfg.scorer_model == "gpt-4o-mini"
    assert cfg.tmp_dir == Path("tmp/skills/benchmark")
    assert cfg.docs_dir == Path("docs/skills/benchmark")


def test_config_env_override(monkeypatch: pytest.MonkeyPatch) -> None:
    """Environment variables should override defaults."""

    monkeypatch.setenv("OPENAI_API_KEY", "test-api-key")
    monkeypatch.setenv("BENCHMARK_LLM_BASE_URL", "http://localhost:11434/v1")
    monkeypatch.setenv("BENCHMARK_LLM_MODEL", "test-model")
    monkeypatch.setenv("BENCHMARK_SCORER_BASE_URL", "http://localhost:11434/v1")
    monkeypatch.setenv("BENCHMARK_SCORER_MODEL", "test-scorer-model")
    monkeypatch.setenv("BENCHMARK_TMP_DIR", "tmp/skills/benchmark-test")
    monkeypatch.setenv("BENCHMARK_DOCS_DIR", "docs/skills/benchmark-test")

    cfg = BenchmarkConfig(_env_file=None)

    assert cfg.api_key == "test-api-key"
    assert cfg.llm_base_url == "http://localhost:11434/v1"
    assert cfg.llm_model == "test-model"
    assert cfg.scorer_base_url == "http://localhost:11434/v1"
    assert cfg.scorer_model == "test-scorer-model"
    assert cfg.tmp_dir == Path("tmp/skills/benchmark-test")
    assert cfg.docs_dir == Path("docs/skills/benchmark-test")


def test_config_loads_from_env_file(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Values in a .env file should load when no env override is set."""

    monkeypatch.chdir(tmp_path)
    env_file = tmp_path / ".env"
    env_file.write_text(
        "OPENAI_API_KEY=from-dotenv\n"
        "BENCHMARK_LLM_BASE_URL=http://localhost:11434/v1\n"
        "BENCHMARK_LLM_MODEL=llama3.2\n",
        encoding="utf-8",
    )
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("BENCHMARK_LLM_BASE_URL", raising=False)
    monkeypatch.delenv("BENCHMARK_LLM_MODEL", raising=False)

    cfg = BenchmarkConfig()

    assert cfg.api_key == "from-dotenv"
    assert cfg.llm_base_url == "http://localhost:11434/v1"
    assert cfg.llm_model == "llama3.2"
