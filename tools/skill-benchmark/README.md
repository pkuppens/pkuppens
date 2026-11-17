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

### On-demand skill discovery (agent sessions)

Search first rather than injecting the tree or every skill into the prompt:

```bash
uv run skill-benchmark find-skill "which skill handles GitHub issues?"
uv run skill-benchmark find-skill "duplicate detection" --limit 3
uv run skill-benchmark load-skill @issue-workflow
uv run skill-benchmark load-skill issue-workflow/issue-check-duplicates/SKILL.md
# Works outside this repository with an explicit skills root:
uv run --project /path/to/pkuppens/tools/skill-benchmark \
  skill-benchmark find-skill "GitHub issues" --skills-dir ~/.claude/skills
```

`find-skill` returns JSON containing only name, description, absolute path, and
relevance score. It uses local BM25 keyword ranking over YAML names/descriptions,
Markdown headings, and the one-line summaries under named `SKILL_TREE.md` headings.
It indexes existing `SKILL.md` files, including nested skills; tree entries without
files are not loadable suggestions. YAML folded/quoted descriptions are supported.
No model, embeddings, API key, network service, or persisted index is needed.

Results default to **five**, configurable from 1–20. Blank, stop-word-only, or
unmatched queries return `[]`; fewer matches are not padded. Scores are relative
ranking, not confidence. Search is lexical (case-insensitive, hyphens split, simple
plural normalization), not semantic: rephrase or use an explicit reference when
synonyms do not match.

For auto-detection, let the agent search with the current task, inspect descriptions,
then load only the best relevant skill (or a small justified set). Do not
automatically inject every result or traverse all sub-skills. If no result fits,
ask for clarification or refine the query; manual activation remains available.
This keeps context bounded without hiding plausible alternatives.

**Agent tool surface:** register these bound Python methods with your agent's tool
dispatcher (or an existing MCP host); no MCP server/transport is bundled:

```python
from pathlib import Path
from skill_benchmark.discovery import SkillIndex

index = SkillIndex(Path("/path/to/pkuppens/skills"))
find_skill = index.find_skill   # (query: str, limit: int = 5) -> list[dict]
load_skill = index.load_skill   # (name: str) -> str
matches = find_skill("which skill handles GitHub issues?")
content = load_skill(matches[0]["path"]) if matches else None
```

The root can be a Cursor, Claude, or Codex skills symlink, or a directory containing
symlinked skill/library directories. Cycles and duplicate directory targets are
skipped. Only point it at **trusted** skill directories: indexed symlinks may lead
outside the root and skill text is instructions, not a security boundary.
Malformed frontmatter reports an error with the file path instead of silently
hiding skills. Construct a new index after adding skills or editing metadata
(the CLI does this per invocation); loading reads the current file content.

`load-skill` / `load_skill` accepts YAML names, `@name`, `/name`, `@/name`, relative
skill paths, and absolute directory or `SKILL.md` paths. Duplicate names require
an explicit path (prefer the search result's path). Only indexed skill files
can be loaded; traversal and arbitrary file reads are rejected. The result is
the unchanged UTF-8 `SKILL.md` text, including frontmatter, just as the benchmark's
`SkillLoader.load(...).content` supplies today.

**Benchmark vs production:** keep full skill injection for controlled baseline /
with-skill comparisons; discovery must not change which reference a benchmark
uses. Production sessions should search metadata and explicitly load selected
skills on demand. Existing `list-skills`, `run`, IDE symlinks, and manual skill
activation are unchanged.

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
uv run skill-benchmark find-skill <query> [--limit 1-20] [--skills-dir PATH]
uv run skill-benchmark load-skill <name-or-path> [--skills-dir PATH]
uv run skill-benchmark run <skill-name> <task-name> [--dry-run] [--base-url URL] [--model NAME] [--scorer-model NAME]
```

## Architecture

| Module | Role |
|--------|------|
| `loader.py` | Load tasks from `docs/skills/benchmark/tasks/` and skills from `skills/` |
| `discovery.py` | Bounded BM25 metadata search and on-demand skill loading for agent tools |
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
