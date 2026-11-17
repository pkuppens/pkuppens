from pathlib import Path

import pytest

from skill_benchmark.discovery import SkillIndex
from skill_benchmark.loader import SkillLoader
from skill_benchmark.paths import find_repo_root


@pytest.fixture
def skills_dir(tmp_path: Path) -> Path:
    root = tmp_path / "skills"
    for folder, name, description, body in [
        ("issues", "issues", "Handles GitHub issues.", "# Issue workflow\n\nSECRET BODY\n"),
        ("issues/triage", "triage", "Refines reports.", "# Triage\n\n## Duplicate detection\n"),
        ("deploy", "deploy", "Deploys services.", "# Deployment\n"),
    ]:
        directory = root / folder
        directory.mkdir(parents=True)
        (directory / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {description}\n---\n\n{body}", encoding="utf-8"
        )
    (root / "SKILL_TREE.md").write_text(
        "### 5. issues\nCoordinates backlog ownership.\n\n"
        "#### 5.1 triage\nChecks ticket reproducibility.\n\n"
        "#### 5.2 unimplemented\nHandles quantum teleportation.\n",
        encoding="utf-8",
    )
    return root


def test_search_returns_ranked_metadata_only(skills_dir: Path) -> None:
    index = SkillIndex(skills_dir)
    matches = index.find_skill("which skill handles GitHub issues?")
    assert matches[0]["name"] == "issues"
    assert matches[0]["description"] == "Handles GitHub issues."
    assert matches[0]["path"] == str(skills_dir / "issues/SKILL.md")
    assert "SECRET BODY" not in str(matches)
    assert "content" not in matches[0]
    assert index.find_skill("github issue") == index.find_skill("github issues")


def test_search_indexes_headings_and_tree_but_not_unimplemented_skills(skills_dir: Path) -> None:
    index = SkillIndex(skills_dir)
    assert index.find_skill("duplicate")[0]["name"] == "triage"
    assert index.find_skill("reproducibility")[0]["name"] == "triage"
    assert index.find_skill("backlog ownership")[0]["name"] == "issues"
    assert index.find_skill("teleportation") == []
    assert index.find_skill("SECRET BODY") == []


def test_search_limits_empty_queries_and_ties(skills_dir: Path) -> None:
    index = SkillIndex(skills_dir)
    assert index.find_skill("") == []
    assert index.find_skill("which skill is it?") == []
    assert index.find_skill("zzzznonexistent") == []
    assert len(index.find_skill("issues triage deploy", limit=1)) == 1
    with pytest.raises(ValueError, match="between 1 and 20"):
        index.find_skill("issues", limit=0)
    with pytest.raises(ValueError, match="between 1 and 20"):
        index.find_skill("issues", limit=21)
    # Equal metadata produces deterministic ordering by relative path.
    (skills_dir / "deploy/SKILL.md").write_bytes((skills_dir / "issues/SKILL.md").read_bytes())
    tied = SkillIndex(skills_dir).find_skill("github")
    assert [Path(match["path"]).parent.name for match in tied] == ["deploy", "issues"]


@pytest.mark.parametrize(
    "reference",
    ["issues", "@issues", "issues/SKILL.md"],
)
def test_load_explicit_references(skills_dir: Path, reference: str) -> None:
    expected = (skills_dir / "issues/SKILL.md").read_text(encoding="utf-8")
    assert SkillIndex(skills_dir).load_skill(reference) == expected


def test_load_nested_and_absolute_paths(skills_dir: Path) -> None:
    index = SkillIndex(skills_dir)
    path = skills_dir / "issues/triage/SKILL.md"
    expected = path.read_text(encoding="utf-8")
    for reference in ("triage", "@triage", "issues/triage", str(path), str(path.parent)):
        assert index.load_skill(reference) == expected


def test_load_rejects_unknown_traversal_and_arbitrary_files(skills_dir: Path) -> None:
    index = SkillIndex(skills_dir)
    for reference in ("../skills/issues", "issues/../../secret", ""):
        with pytest.raises(ValueError, match="Invalid skill reference"):
            index.load_skill(reference)
    for reference in ("not-a-skill", str(skills_dir / "SKILL_TREE.md"), "/etc/passwd"):
        with pytest.raises(FileNotFoundError, match="Skill not found"):
            index.load_skill(reference)


def test_duplicate_names_require_explicit_path(skills_dir: Path) -> None:
    (skills_dir / "deploy/SKILL.md").write_bytes((skills_dir / "issues/SKILL.md").read_bytes())
    index = SkillIndex(skills_dir)
    with pytest.raises(ValueError, match="Ambiguous"):
        index.load_skill("@issues")
    assert index.load_skill("deploy") == (skills_dir / "deploy/SKILL.md").read_text()
    assert index.load_skill("issues/SKILL.md") == (skills_dir / "issues/SKILL.md").read_text()


@pytest.mark.parametrize("ide", [".cursor", ".claude", ".codex"])
def test_symlinked_roots_and_children(skills_dir: Path, tmp_path: Path, ide: str) -> None:
    ide_dir = tmp_path / ide
    ide_dir.mkdir()
    link = ide_dir / "skills"
    link.symlink_to(skills_dir, target_is_directory=True)
    assert SkillIndex(link).load_skill("@triage") == SkillIndex(skills_dir).load_skill("triage")
    link.unlink()
    link.mkdir()
    (link / "library").symlink_to(skills_dir, target_is_directory=True)
    # Follow trusted child links, but terminate on cycles and deduplicate aliases.
    (skills_dir / "loop").symlink_to(skills_dir, target_is_directory=True)
    (link / "alias").symlink_to(skills_dir, target_is_directory=True)
    index = SkillIndex(link)
    assert len(index.find_skill("github")) == 1
    assert index.load_skill(str(link / "library/issues")) == index.load_skill("@issues")
    assert index.find_skill("reproducibility")[0]["name"] == "triage"


def test_multiline_yaml_and_missing_tree(skills_dir: Path) -> None:
    path = skills_dir / "deploy/SKILL.md"
    path.write_text(
        '---\nname: "deploy"\ndescription: >-\n  Deploys services:\n  safely.\n---\n# Deploy\n'
    )
    (skills_dir / "SKILL_TREE.md").unlink()
    assert SkillIndex(skills_dir).find_skill("services")[0]["description"] == (
        "Deploys services: safely."
    )


@pytest.mark.parametrize(
    "text",
    ["# No metadata\n", "---\nname: deploy\n---\n", "---\nname: [bad yaml\n---\n"],
)
def test_invalid_metadata_reports_file(skills_dir: Path, text: str) -> None:
    path = skills_dir / "deploy/SKILL.md"
    path.write_text(text)
    with pytest.raises(ValueError, match=str(path)):
        SkillIndex(skills_dir)


def test_empty_and_missing_directory(tmp_path: Path) -> None:
    assert SkillIndex(tmp_path).find_skill("github") == []
    with pytest.raises(FileNotFoundError, match="Skills directory"):
        SkillIndex(tmp_path / "missing")


def test_repository_acceptance_and_benchmark_content_unchanged() -> None:
    root = find_repo_root()
    index = SkillIndex(root / "skills")
    matches = index.find_skill("which skill handles GitHub issues?")
    assert "issue-workflow" in [match["name"] for match in matches]
    assert index.load_skill("@issue-workflow") == SkillLoader(root).load("issue-workflow").content
    assert index.find_skill("find skill", limit=20)
