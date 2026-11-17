import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from skill_benchmark.cli import cli
from skill_benchmark.paths import find_repo_root


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


def test_cli_find_skill_metadata() -> None:
    result = CliRunner().invoke(cli, ["find-skill", "which skill handles GitHub issues?"])
    assert result.exit_code == 0, result.output
    matches = json.loads(result.output)
    assert len(matches) <= 5
    assert "issue-workflow" in [match["name"] for match in matches]
    assert all("content" not in match for match in matches)


def test_cli_load_skill_exact_content() -> None:
    result = CliRunner().invoke(cli, ["load-skill", "@issue-workflow"])
    expected = (find_repo_root() / "skills/issue-workflow/SKILL.md").read_text(encoding="utf-8")
    assert result.exit_code == 0, result.output
    assert result.output == expected


def test_cli_discovery_with_symlink_outside_repo(tmp_path: Path, monkeypatch) -> None:
    root = find_repo_root()
    link = tmp_path / "linked-skills"
    try:
        link.symlink_to(root / "skills", target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"cannot create symlinks here: {exc}")
    monkeypatch.chdir(tmp_path)
    result = CliRunner().invoke(cli, ["find-skill", "github issues", "--skills-dir", str(link)])
    assert result.exit_code == 0, result.output
    assert json.loads(result.output)
    result = CliRunner().invoke(cli, ["load-skill", "@issue-workflow", "--skills-dir", str(link)])
    assert result.exit_code == 0, result.output
    assert result.output == (root / "skills/issue-workflow/SKILL.md").read_text(encoding="utf-8")


def test_cli_discovery_errors() -> None:
    runner = CliRunner()
    missing = runner.invoke(cli, ["load-skill", "no-such-skill"])
    assert missing.exit_code != 0
    assert "Skill not found" in missing.output
    invalid = runner.invoke(cli, ["find-skill", "github", "--limit", "21"])
    assert invalid.exit_code != 0
    assert runner.invoke(cli, ["find-skill", "zzzznonexistent"]).output.strip() == "[]"
