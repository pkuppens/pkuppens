# skill-benchmark

Skill benchmark is a small Python toolset to measure whether a skill improves agent output quality.

The benchmark compares two runs of the same task:

1. **Baseline**: run without the skill content
2. **With skill**: run with the skill content

This makes skill quality visible and discussable with evidence instead of opinion.

## Why this exists

This repo has many skills. Without a benchmark flow, it is hard to answer questions like:

- "Did this skill update actually help?"
- "Which skills have the biggest impact?"
- "Did a refactor reduce quality?"

The benchmark package helps generate repeatable evidence so pull requests can include concrete results.

## User stories

- As a skill author, I want to compare baseline and with-skill output, so I can prove my skill adds value.
- As a reviewer, I want to see structured benchmark evidence, so I can approve changes with more confidence.
- As a maintainer, I want a repeatable benchmark workflow, so regressions are detected early.
- As a contributor, I want clear extension points, so I can add new tasks, skills, and scoring logic safely.

## Current scope (this bootstrap step)

This first version provides the foundation:

- Configuration loading (`BenchmarkConfig`)
- OpenAI-compatible provider wrapper (`LLMProvider`)
- CLI skeleton for future commands (`list-tasks`, `list-skills`, `run`)
- Unit tests for config and provider behavior

Follow-up issues add loaders, scoring, reports, and full orchestration.

## Quick start

### 1) Setup

```bash
cd tools/skill-benchmark
uv sync
```

### 2) Run checks

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

### 3) Explore the CLI skeleton

```bash
uv run python -m skill_benchmark.cli --help
```

At this stage, command bodies are intentionally placeholders and will raise a "Not implemented yet" message.

## Configuration

Settings load from **environment variables** and from a **`.env` file** in `tools/skill-benchmark/` (gitignored). Copy `.env.example` to `.env` for local Ollama runs.

```bash
cd tools/skill-benchmark
cp .env.example .env
# edit .env — model names, base URL, API key
```

See `src/skill_benchmark/README.md` for the end-to-end benchmark workflow and example task.

### Core LLM settings

- `OPENAI_API_KEY`: API key for OpenAI-compatible endpoints
- `BENCHMARK_LLM_BASE_URL`: base URL for generation model endpoint
- `BENCHMARK_LLM_MODEL`: model name for generation calls
- `BENCHMARK_SCORER_BASE_URL`: base URL for scorer model endpoint
- `BENCHMARK_SCORER_MODEL`: model name for scorer calls

### Paths

- `BENCHMARK_TMP_DIR`: scratch output location (default: `tmp/skills/benchmark`)
- `BENCHMARK_DOCS_DIR`: report output location (default: `docs/skills/benchmark`)

### Example (PowerShell)

```powershell
$env:OPENAI_API_KEY="your-key"
$env:BENCHMARK_LLM_BASE_URL="http://localhost:11434/v1"
$env:BENCHMARK_LLM_MODEL="qwen2.5-coder:14b"
```

## How to extend or change

### Add a new benchmark task

1. Add a task markdown file under `docs/skills/benchmark/tasks/`
2. Keep task prompt and expected coverage explicit
3. Add loader tests once loader implementation is added

### Add a new provider behavior

1. Extend `LLMProvider` in `src/skill_benchmark/provider.py`
2. Keep API surface backward compatible (`complete(...) -> LLMResponse`)
3. Add tests in `tests/test_provider.py`

### Add new CLI command behavior

1. Implement command flow in `src/skill_benchmark/cli.py`
2. Keep command help text user-focused
3. Add command tests and README usage examples

## Design notes

- This package uses OpenAI-compatible APIs, which allows local and cloud providers behind one interface.
- Provider injection in tests avoids real API calls and keeps unit tests fast.
- Configuration uses environment variables to keep secrets out of code and out of git history.
