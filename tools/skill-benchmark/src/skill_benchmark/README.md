# skill_benchmark package

## Purpose

This package runs **skill benchmarks**: the same task is executed twice so you can compare quality with and without skill guidance.

## Goal

Produce evidence that a skill improves output (structure, completeness, correctness) instead of relying on subjective review.

## End-to-end workflow (target)

When fully wired (#102–#104), a benchmark run looks like this:

```text
1. Pick a task prompt (e.g. from docs/skills/benchmark/tasks/)
2. Pick a skill to test (e.g. issue-workflow)
3. Generate baseline output (prompt only, no skill text)
4. Generate with-skill output (same prompt + SKILL.md content)
5. Score both outputs independently (4 dimensions, 1–5 each)
6. Write a markdown report with verdict and deltas
```

Outputs:

- Scratch: `tmp/skills/benchmark/<skill-name>/output-baseline.md`, `output-with-skill.md`
- Report: `docs/skills/benchmark/<skill-name>/report.md`

## Example task (markdown only, no GitHub issue created)

**Prompt:** “Create a markdown specification for role-based access control (RBAC) for a web application.”

| Run | What the agent gets | Expected difference |
|-----|---------------------|---------------------|
| Baseline | Task prompt only | Generic RBAC doc; may miss sections |
| With skill | Same prompt + `issue-workflow` / issue-acceptance-criteria skill | Clear sections: goal, tasks, acceptance criteria, out of scope, estimate |

We compare markdown artefacts only. **Do not** call `gh issue create` during the benchmark.

A future task file may formalize this as `rbac-spec.md` under `docs/skills/benchmark/tasks/`.

## Modules in this directory

| Module | Role |
|--------|------|
| `config.py` | Settings from environment and `.env` (Ollama, models, paths) |
| `provider.py` | OpenAI-compatible LLM calls |
| `cli.py` | User commands (`run`, `list-tasks`, `list-skills`) — scaffold in #101 |

## Bootstrap status (#101)

Loaders, generator, scorer, and orchestrator are added in follow-up issues. This directory already provides config + provider + CLI skeleton.

See also the package README at `tools/skill-benchmark/README.md`.
