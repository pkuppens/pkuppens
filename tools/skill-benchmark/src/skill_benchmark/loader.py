"""Load benchmark tasks and skill markdown from the repository.

``TaskLoader`` reads versioned prompts from ``docs/skills/benchmark/tasks/``.
``SkillLoader`` reads ``SKILL.md`` from ``skills/<name>/``.

Deliverable: parsed :class:`~skill_benchmark.models.TaskPrompt` and
:class:`~skill_benchmark.models.SkillContent` objects for agents and the runner.
"""

from __future__ import annotations

import re
from pathlib import Path

from .models import SkillContent, TaskPrompt
from .paths import find_repo_root


class TaskLoader:
    """Discover and parse benchmark task markdown files."""

    def __init__(self, repo_root: Path | None = None) -> None:
        """Create a task loader rooted at the repository.

        Args:
            repo_root (Path | None): Repository root. When omitted, it is
                discovered automatically.
        """

        self._repo_root = repo_root or find_repo_root()
        self._tasks_dir = self._repo_root / "docs" / "skills" / "benchmark" / "tasks"

    def list_tasks(self) -> list[str]:
        """Return sorted task names (filename stems without .md)."""

        if not self._tasks_dir.is_dir():
            return []
        return sorted(path.stem for path in self._tasks_dir.glob("*.md"))

    def load(self, task_name: str) -> TaskPrompt:
        """Load one task by name.

        Args:
            task_name (str): Task file stem (for example `issue-creation`).

        Returns:
            TaskPrompt: Parsed task prompt and expected coverage.

        Raises:
            FileNotFoundError: If the task file does not exist.
            ValueError: If required sections are missing.
        """

        task_path = self._tasks_dir / f"{task_name}.md"
        if not task_path.is_file():
            raise FileNotFoundError(f"Task not found: {task_name} ({task_path})")

        text = task_path.read_text(encoding="utf-8")
        prompt = _extract_section(text, "Task prompt")
        expected_coverage = _extract_section(text, "Expected coverage")
        skill_under_test = _extract_metadata_field(text, "Skill under test")

        if not prompt:
            raise ValueError(f"Task {task_name} is missing a '## Task prompt' section.")

        return TaskPrompt(
            name=task_name,
            prompt=prompt.strip(),
            expected_coverage=expected_coverage.strip(),
            skill_under_test=skill_under_test,
        )


class SkillLoader:
    """Discover and load SKILL.md files from the skills tree."""

    def __init__(self, repo_root: Path | None = None) -> None:
        """Create a skill loader rooted at the repository.

        Args:
            repo_root (Path | None): Repository root. When omitted, it is
                discovered automatically.
        """

        self._repo_root = repo_root or find_repo_root()
        self._skills_dir = self._repo_root / "skills"

    def list_skills(self) -> list[str]:
        """Return sorted skill directory names that contain SKILL.md."""

        if not self._skills_dir.is_dir():
            return []

        names: set[str] = set()
        for skill_md in self._skills_dir.rglob("SKILL.md"):
            relative = skill_md.parent.relative_to(self._skills_dir)
            if relative.parts:
                names.add(relative.parts[0])
        return sorted(names)

    def load(self, skill_name: str) -> SkillContent:
        """Load the top-level skill markdown for a skill directory name.

        Args:
            skill_name (str): First path segment under `skills/` (for example
                `issue-workflow`).

        Returns:
            SkillContent: Skill name and markdown body.

        Raises:
            FileNotFoundError: If `skills/<skill_name>/SKILL.md` does not exist.
        """

        skill_path = self._skills_dir / skill_name / "SKILL.md"
        if not skill_path.is_file():
            raise FileNotFoundError(f"Skill not found: {skill_name} ({skill_path})")

        return SkillContent(name=skill_name, content=skill_path.read_text(encoding="utf-8"))


def _extract_section(text: str, heading: str) -> str:
    """Return body text for a level-2 markdown heading."""

    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def _extract_metadata_field(text: str, field_name: str) -> str | None:
    """Return a bold metadata field value from task markdown."""

    pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.+)"
    match = re.search(pattern, text)
    if not match:
        return None
    return match.group(1).strip()
