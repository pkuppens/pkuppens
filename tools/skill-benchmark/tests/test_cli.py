from click.testing import CliRunner

from skill_benchmark.cli import cli


def test_cli_list_tasks_includes_three_tasks() -> None:
    """list-tasks should print at least three known benchmark tasks."""

    result = CliRunner().invoke(cli, ["list-tasks"])
    assert result.exit_code == 0
    names = result.output.strip().splitlines()
    assert "issue-creation" in names
    assert "deployment-checklist" in names
    assert "adr-authoring" in names


def test_cli_dry_run_validates_without_api_key() -> None:
    """dry-run should succeed without OPENAI_API_KEY."""

    result = CliRunner().invoke(
        cli,
        ["run", "issue-workflow", "issue-creation", "--dry-run"],
    )
    assert result.exit_code == 0
    assert "Dry run OK" in result.output


def test_cli_unknown_task_fails() -> None:
    """Unknown task names should produce a non-zero exit code."""

    result = CliRunner().invoke(cli, ["run", "issue-workflow", "missing-task", "--dry-run"])
    assert result.exit_code != 0
    assert "Unknown task" in result.output
