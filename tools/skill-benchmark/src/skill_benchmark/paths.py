"""Resolve repository paths for benchmark loaders and output writers."""

from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    """Locate the repository root by walking up for `skills/SKILL_TREE.md`.

    Args:
        start (Path | None): Directory to start from. Defaults to the current
            working directory.

    Returns:
        Path: Absolute path to the repository root.

    Raises:
        FileNotFoundError: If no repository root marker is found.
    """

    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "skills" / "SKILL_TREE.md").is_file():
            return candidate
    raise FileNotFoundError(
        "Could not find repository root (expected skills/SKILL_TREE.md in a parent directory)."
    )
