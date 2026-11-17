"""On-demand skill tools: search metadata first, load full markdown only on request."""

from __future__ import annotations

import math
import os
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml

from .paths import find_repo_root

_STOP_WORDS = set(
    "a an and are for handles how i in is it of skill skills the to what which".split()
)


def _tokens(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [
        word[:-1] if len(word) > 3 and word.endswith("s") and not word.endswith("ss") else word
        for word in words
        if word not in _STOP_WORDS
    ]


def _tree_summaries(path: Path) -> dict[str, str]:
    """Read the canonical tree's named headings and their one-line summaries."""

    if not path.is_file():
        return {}
    summaries = {}
    name = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            match = re.fullmatch(r"#{3,6}\s+(?:\d+(?:\.\d+)*\.?\s+)?([\w-]+)\s*", line)
            name = match[1] if match else None
        elif name and line.strip() and not line.startswith("//"):
            summaries[name] = line.strip()
            name = None
    return summaries


@dataclass(frozen=True)
class _Skill:
    name: str
    description: str
    path: Path
    relative_path: str
    terms: Counter[str]


class SkillIndex:
    """Index a trusted skills root, including nested and symlinked directories.

    Expose the bound ``find_skill`` and ``load_skill`` methods as agent tools.
    Construct a new index to pick up added files or changed metadata.
    """

    def __init__(self, skills_dir: Path | None = None) -> None:
        self.root = (skills_dir or find_repo_root() / "skills").expanduser().resolve()
        if not self.root.is_dir():
            raise FileNotFoundError(f"Skills directory not found: {self.root}")
        summaries: dict[str, str] = {}
        self._skills: list[_Skill] = []
        seen: set[Path] = set()
        for directory, children, files in os.walk(self.root, followlinks=True):
            folder = Path(directory)
            resolved = folder.resolve()
            if resolved in seen:
                children[:] = []
                continue
            seen.add(resolved)
            children[:] = sorted(child for child in children if not child.startswith("."))
            if "SKILL_TREE.md" in files:
                summaries.update(_tree_summaries(folder / "SKILL_TREE.md"))
            if "SKILL.md" not in files:
                continue
            path = folder / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
            try:
                metadata = yaml.safe_load(frontmatter[1]) if frontmatter else None
            except yaml.YAMLError as exc:
                raise ValueError(f"Invalid skill frontmatter: {path}") from exc
            if (
                not isinstance(metadata, dict)
                or not isinstance(metadata.get("name"), str)
                or not re.fullmatch(r"[a-z0-9-]{1,64}", metadata["name"])
                or not isinstance(metadata.get("description"), str)
                or not metadata["description"].strip()
            ):
                raise ValueError(f"Skill requires a valid name and description: {path}")
            name, description = metadata["name"], metadata["description"]
            headings = " ".join(re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE))
            terms = Counter(_tokens(f"{name} {description} {headings} {summaries.get(name, '')}"))
            self._skills.append(
                _Skill(
                    name,
                    description,
                    path.resolve(),
                    folder.relative_to(self.root).as_posix(),
                    terms,
                )
            )
        self._skills.sort(key=lambda skill: skill.relative_path)
        self._document_frequency = Counter(term for skill in self._skills for term in skill.terms)
        self._average_length = (
            sum(skill.terms.total() for skill in self._skills) / len(self._skills)
            if self._skills
            else 1
        )

    def find_skill(self, query: str, limit: int = 5) -> list[dict[str, str | float]]:
        """Return at most ``limit`` metadata matches, ranked by BM25 (no bodies).

        Empty or unmatched queries return no suggestions. Limit must be 1–20;
        scores are relative relevance, not confidence or an activation threshold.
        """

        if not 1 <= limit <= 20:
            raise ValueError("limit must be between 1 and 20")
        query_terms = sorted(set(_tokens(query)))
        ranked = []
        for skill in self._skills:
            score = 0.0
            for term in query_terms:
                frequency = skill.terms[term]
                if not frequency:
                    continue
                df = self._document_frequency[term]
                idf = math.log(1 + (len(self._skills) - df + 0.5) / (df + 0.5))
                normalization = 1.5 * (0.25 + 0.75 * skill.terms.total() / self._average_length)
                score += idf * frequency * 2.5 / (frequency + normalization)
            if score > 0:
                ranked.append((score, skill))
        ranked.sort(key=lambda item: (-item[0], item[1].relative_path))
        return [
            {
                "name": skill.name,
                "description": skill.description,
                "path": str(skill.path),
                "score": round(score, 6),
            }
            for score, skill in ranked[:limit]
        ]

    def load_skill(self, name: str) -> str:
        """Return unchanged SKILL.md text by name, @name, or path.

        A path is absolute or relative to the skills root. Ambiguous names
        require a path. Only indexed files may be loaded.
        """

        reference = name.strip().removeprefix("@")
        if not reference or ".." in Path(reference).parts:
            raise ValueError(f"Invalid skill reference: {name}")
        reference = reference.replace("\\", "/")
        short = reference.removesuffix("/SKILL.md").rstrip("/")
        path = self.root / reference
        candidates = {path.resolve(), (path / "SKILL.md").resolve()}
        path_matches = [skill for skill in self._skills if skill.path in candidates]
        matches = (
            path_matches
            if "/" in reference and path_matches
            else [skill for skill in self._skills if short in (skill.name, skill.relative_path)]
        )
        if not matches:
            raise FileNotFoundError(f"Skill not found in index: {name}")
        if len(matches) > 1:
            paths = ", ".join(skill.relative_path for skill in matches)
            raise ValueError(f"Ambiguous skill reference {name!r}; use a path: {paths}")
        return matches[0].path.read_text(encoding="utf-8")
