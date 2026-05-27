from pathlib import Path

import pytest

from skill_benchmark.loader import SkillLoader, TaskLoader


def test_task_loader_lists_known_tasks(repo_root: Path) -> None:
    """Task loader should discover committed benchmark tasks."""

    names = TaskLoader(repo_root).list_tasks()
    assert "issue-creation" in names
    assert "deployment-checklist" in names
    assert "adr-authoring" in names
    assert len(names) >= 3


def test_task_loader_parses_issue_creation(repo_root: Path) -> None:
    """Task loader should parse prompt and expected coverage sections."""

    task = TaskLoader(repo_root).load("issue-creation")
    assert task.name == "issue-creation"
    assert "hybrid retrieval" in task.prompt
    assert "Actionable title" in task.expected_coverage
    assert (
        task.skill_under_test
        == "issue-workflow (e.g. issue-acceptance-criteria, issue-check-duplicates)"
    )


def test_skill_loader_lists_and_loads_issue_workflow(repo_root: Path) -> None:
    """Skill loader should discover and load top-level skills."""

    loader = SkillLoader(repo_root)
    assert "issue-workflow" in loader.list_skills()

    skill = loader.load("issue-workflow")
    assert skill.name == "issue-workflow"
    assert "name: issue-workflow" in skill.content


def test_task_loader_missing_task_raises(repo_root: Path) -> None:
    """Unknown task names should raise FileNotFoundError."""

    with pytest.raises(FileNotFoundError, match="missing-task"):
        TaskLoader(repo_root).load("missing-task")


@pytest.fixture
def repo_root() -> Path:
    """Return repository root for integration-style loader tests."""

    from skill_benchmark.paths import find_repo_root

    return find_repo_root()
