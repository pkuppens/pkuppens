"""CLI for the skill benchmark harness.

Purpose:
    Give maintainers simple commands to list tasks/skills and run benchmarks.

What it helps with:
    - Discover which benchmark tasks and skills exist
    - Run baseline vs with-skill comparisons (once #104 lands)
    - Produce evidence files for pull requests

This module is a thin wrapper around Click. You do not need to know Click internals
to use it: run `uv run python -m skill_benchmark.cli --help`.
"""

import click


@click.group()
def cli() -> None:
    """Skill benchmark harness — compare agent output with and without skills.

    Goal:
        Measure whether a skill improves task output quality using repeatable runs.

    What you can do (today vs planned):
        - Today (#101): show help; sub-commands are placeholders
        - #102: list tasks and skills from the repo
        - #104: run full benchmark and write reports

    Run from: tools/skill-benchmark/
    """


@cli.command("list-tasks")
def list_tasks() -> None:
    """List benchmark task prompts available under docs/skills/benchmark/tasks/.

    Purpose:
        Show which tasks you can run against a skill.

    Planned behavior (#102):
        Print one task name per line (e.g. issue-creation, rbac-spec).

    Examples (expected once implemented):

        $ uv run python -m skill_benchmark.cli list-tasks
        issue-creation
        rbac-spec

    Exit code: 0 on success.
    """

    raise click.ClickException("Not implemented yet.")


@cli.command("list-skills")
def list_skills() -> None:
    """List skills that can be benchmarked from the skills/ tree.

    Purpose:
        Show skill directory names you can pass to `run`.

    Planned behavior (#102):
        Discover directories containing SKILL.md under skills/.

    Examples (expected once implemented):

        $ uv run python -m skill_benchmark.cli list-skills
        issue-workflow
        deployment-release

    Exit code: 0 on success.
    """

    raise click.ClickException("Not implemented yet.")


@cli.command("run")
@click.argument("skill_name", required=True)
@click.argument("task_name", required=True)
def run_benchmark(skill_name: str, task_name: str) -> None:
    """Run one full benchmark: baseline and with-skill, then score and report.

    Purpose:
        Produce comparable evidence for a single skill on a single task.

    Planned behavior (#104):
        1. Load task prompt and skill SKILL.md
        2. Call LLM twice (isolated contexts)
        3. Score each output
        4. Write tmp outputs and docs/skills/benchmark/<skill>/report.md

    Examples (expected once implemented):

        $ uv run python -m skill_benchmark.cli run issue-workflow issue-creation

    Expected console output (summary):
        - Paths to output-baseline.md and output-with-skill.md
        - Path to report.md
        - Verdict: significant improvement | marginal | no improvement

    Expected artefacts:
        - tmp/skills/benchmark/issue-workflow/output-baseline.md
        - tmp/skills/benchmark/issue-workflow/output-with-skill.md
        - docs/skills/benchmark/issue-workflow/report.md

    Exit code: 0 on success; non-zero if LLM or scoring fails.
    """

    raise click.ClickException(f"Not implemented yet (skill={skill_name}, task={task_name}).")


if __name__ == "__main__":
    cli()
