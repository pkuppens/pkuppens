"""Command-line interface for the skill benchmark harness.

Commands: ``list-tasks``, ``list-skills``, ``find-skill``, ``load-skill``, and ``run`` (with ``--dry-run``,
``--base-url``, ``--model``, ``--scorer-model`` overrides).

Deliverable: operator entry point installed as the ``skill-benchmark`` console script.
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

import click

from .config import BenchmarkConfig
from .discovery import SkillIndex
from .loader import SkillLoader, TaskLoader
from .paths import find_repo_root
from .runner import BenchmarkRunner


def _build_config(
    base_url: str | None,
    model: str | None,
    scorer_model: str | None,
) -> BenchmarkConfig:
    """Build config with optional CLI overrides."""

    updates: dict[str, object] = {"_env_file": None}
    if base_url:
        updates["llm_base_url"] = base_url
        updates["scorer_base_url"] = base_url
    if model:
        updates["llm_model"] = model
    if scorer_model:
        updates["scorer_model"] = scorer_model
    return BenchmarkConfig(**updates)


@click.group()
def cli() -> None:
    """Skill benchmark harness — compare agent output with and without skills."""


@cli.command("list-tasks")
def list_tasks() -> None:
    """List benchmark task prompts available under docs/skills/benchmark/tasks/."""

    repo_root = find_repo_root()
    for name in TaskLoader(repo_root).list_tasks():
        click.echo(name)


@cli.command("list-skills")
def list_skills() -> None:
    """List top-level skills discoverable under skills/."""

    repo_root = find_repo_root()
    for name in SkillLoader(repo_root).list_skills():
        click.echo(name)


@cli.command("find-skill")
@click.argument("query")
@click.option("--limit", type=click.IntRange(1, 20), default=5, show_default=True)
@click.option(
    "--skills-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=None,
    help="Skills root or IDE symlink. Defaults to this repository's skills/.",
)
def find_skill(query: str, limit: int, skills_dir: Path | None) -> None:
    """Search skill metadata without loading skill bodies into agent context."""

    try:
        matches = SkillIndex(skills_dir).find_skill(query, limit)
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc
    click.echo(json.dumps(matches, ensure_ascii=False, indent=2))


@cli.command("load-skill")
@click.argument("name")
@click.option(
    "--skills-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=None,
    help="Skills root or IDE symlink. Defaults to this repository's skills/.",
)
def load_skill(name: str, skills_dir: Path | None) -> None:
    """Load exact SKILL.md content by name, @reference, or explicit path."""

    try:
        content = SkillIndex(skills_dir).load_skill(name)
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc
    click.echo(content, nl=False)


@cli.command("run")
@click.argument("skill_name", required=True)
@click.argument("task_name", required=True)
@click.option("--base-url", default=None, help="Override LLM and scorer base URL.")
@click.option("--model", default=None, help="Override generation model name.")
@click.option("--scorer-model", default=None, help="Override scorer model name.")
@click.option(
    "--dry-run",
    is_flag=True,
    help="Validate task/skill paths and config without calling the LLM.",
)
def run_benchmark(
    skill_name: str,
    task_name: str,
    base_url: str | None,
    model: str | None,
    scorer_model: str | None,
    dry_run: bool,
) -> None:
    """Run one full benchmark: baseline and with-skill, then score and report."""

    repo_root = find_repo_root()
    task_loader = TaskLoader(repo_root)
    skill_loader = SkillLoader(repo_root)

    if task_name not in task_loader.list_tasks():
        raise click.ClickException(f"Unknown task: {task_name}")
    if skill_name not in skill_loader.list_skills():
        raise click.ClickException(f"Unknown skill: {skill_name}")

    config = _build_config(base_url, model, scorer_model)

    if dry_run:
        tmp_dir = repo_root / config.tmp_dir if not config.tmp_dir.is_absolute() else config.tmp_dir
        docs_dir = (
            repo_root / config.docs_dir if not config.docs_dir.is_absolute() else config.docs_dir
        )
        click.echo(f"Repo root: {repo_root}")
        click.echo(f"Task: {task_name}")
        click.echo(f"Skill: {skill_name}")
        click.echo(f"LLM: {config.llm_model} @ {config.llm_base_url}")
        click.echo(f"Scorer: {config.scorer_model} @ {config.scorer_base_url}")
        click.echo(f"Tmp dir: {tmp_dir.resolve()}")
        click.echo(f"Docs dir: {docs_dir.resolve()}")
        click.echo("Dry run OK — no LLM calls made.")
        return

    if not config.api_key:
        raise click.ClickException(
            "OPENAI_API_KEY is required for benchmark runs (or use --dry-run)."
        )

    runner = BenchmarkRunner(config, repo_root=repo_root)

    comparison = asyncio.run(runner.run(skill_name, task_name))
    report_path = runner.resolve_docs_dir() / skill_name / "report.md"
    tmp_dir = runner.resolve_tmp_dir() / skill_name

    click.echo(f"Baseline output: {tmp_dir / 'output-baseline.md'}")
    click.echo(f"With-skill output: {tmp_dir / 'output-with-skill.md'}")
    click.echo(f"Report: {report_path}")
    click.echo(f"Verdict: {comparison.verdict} (delta {comparison.delta:+d})")


if __name__ == "__main__":
    cli()
