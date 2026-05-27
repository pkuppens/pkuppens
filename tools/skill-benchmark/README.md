# skill-benchmark

Skill benchmark is a Python toolset to measure whether a skill improves agent output quality.

The benchmark compares two runs of the same task:

1. **Baseline**: run without the skill content
2. **With skill**: run with the skill content

This makes skill quality visible and discussable with evidence instead of opinion.

## Quick start

### 1) Setup

```bash
cd tools/skill-benchmark
uv sync
cp .env.example .env   # optional: local Ollama defaults
```

### 2) Run checks

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

### 3) Explore tasks and skills

From the repository root (or any subdirectory under it):

```bash
cd tools/skill-benchmark
uv run skill-benchmark list-tasks
uv run skill-benchmark list-skills
```

### 4) Dry-run (no LLM calls)

```bash
uv run skill-benchmark run issue-workflow issue-creation --dry-run
```

### 5) Full benchmark run

Requires `OPENAI_API_KEY` (or a compatible local endpoint such as Ollama):

```bash
uv run skill-benchmark run issue-workflow issue-creation \
  --base-url http://localhost:11434/v1 \
  --model qwen2.5-coder:14b \
  --scorer-model qwen2.5-coder:14b
```

**Outputs:**

| Artefact | Location |
|----------|----------|
| Baseline output | `tmp/skills/benchmark/<skill>/output-baseline.md` |
| With-skill output | `tmp/skills/benchmark/<skill>/output-with-skill.md` |
| Report | `docs/skills/benchmark/<skill>/report.md` |

## Configuration

Settings load from environment variables and from `.env` in `tools/skill-benchmark/`.

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | API key for OpenAI-compatible endpoints |
| `BENCHMARK_LLM_BASE_URL` | Generation model base URL |
| `BENCHMARK_LLM_MODEL` | Generation model name |
| `BENCHMARK_SCORER_BASE_URL` | Scorer model base URL |
| `BENCHMARK_SCORER_MODEL` | Scorer model name |
| `BENCHMARK_TMP_DIR` | Scratch output (default: `tmp/skills/benchmark`) |
| `BENCHMARK_DOCS_DIR` | Report output (default: `docs/skills/benchmark`) |

Paths are resolved relative to the repository root (directory containing `skills/SKILL_TREE.md`).

## CLI reference

```bash
uv run skill-benchmark list-tasks
uv run skill-benchmark list-skills
uv run skill-benchmark run <skill-name> <task-name> [--dry-run] [--base-url URL] [--model NAME] [--scorer-model NAME]
```

## Architecture

| Module | Role |
|--------|------|
| `loader.py` | Load tasks from `docs/skills/benchmark/tasks/` and skills from `skills/` |
| `agents/generator.py` | Baseline and with-skill LLM generation (isolated contexts) |
| `agents/scorer.py` | Four-dimension JSON scoring via separate scorer model |
| `report.py` | Markdown report matching `docs/skills/benchmark/*/report.md` format |
| `runner.py` | End-to-end orchestration and artefact persistence |

## Verdict thresholds

| Delta (skilled − baseline) | Verdict |
|----------------------------|---------|
| ≥ +4 | significant improvement |
| +1 to +3 | marginal |
| ≤ 0 | no improvement |

## Design notes

- OpenAI-compatible APIs allow local (Ollama) and cloud providers behind one interface.
- Baseline and with-skill runs use separate message lists (no context contamination).
- The scorer evaluates each output independently (no side-by-side bias).
- Provider injection in tests avoids real API calls.

See also [validation/skill-benchmark](../../skills/validation/skill-benchmark/SKILL.md) for the manual benchmark rubric.
