"""CLI entry points for skill benchmark workflows.

Commands are intentionally scaffolded in this bootstrap stage. Later issues
add task loading, generation, scoring, and report creation behavior.
"""

import click


@click.group()
def cli() -> None:
    """Skill benchmark harness CLI.

    This is a bootstrap skeleton; sub-commands will be implemented in follow-up
    benchmark sub-issues (#102–#104).
    """


@cli.command("list-tasks")
def list_tasks() -> None:
    """List available benchmark tasks.

    Placeholder implementation (loaders and tasks are added in #102).
    """

    raise click.ClickException("Not implemented yet.")


@cli.command("list-skills")
def list_skills() -> None:
    """List available skills that can be benchmarked.

    Placeholder implementation (task/skill loaders are added in #102).
    """

    raise click.ClickException("Not implemented yet.")


@cli.command("run")
@click.argument("skill_name", required=True)
@click.argument("task_name", required=True)
def run_benchmark(skill_name: str, task_name: str) -> None:
    """Run a full benchmark (baseline vs with-skill).

    Placeholder implementation; orchestration and execution are added in #104.
    """

    raise click.ClickException(f"Not implemented yet (skill={skill_name}, task={task_name}).")


if __name__ == "__main__":
    cli()
