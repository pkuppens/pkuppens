from pathlib import Path

import pytest

from skill_benchmark.agents.generator import GeneratorAgent
from skill_benchmark.agents.scorer import ScorerAgent
from skill_benchmark.config import BenchmarkConfig
from skill_benchmark.models import (
    DimensionScore,
    GenerationResult,
    ScoringResult,
    SkillContent,
    TaskPrompt,
)
from skill_benchmark.runner import BenchmarkRunner


class _StubGenerator(GeneratorAgent):
    def __init__(self) -> None:
        pass

    async def generate(
        self, task: TaskPrompt, skill: SkillContent | None = None
    ) -> GenerationResult:
        label = "with-skill" if skill else "baseline"
        return GenerationResult(output=f"{label} output for {task.name}", model="stub")


class _StubScorer(ScorerAgent):
    def __init__(self) -> None:
        pass

    async def score(self, task: TaskPrompt, output: str) -> ScoringResult:
        if output.startswith("baseline"):
            return ScoringResult(
                coverage=DimensionScore(2, "b"),
                specificity=DimensionScore(2, "b"),
                correctness=DimensionScore(3, "b"),
                completeness=DimensionScore(3, "b"),
            )
        return ScoringResult(
            coverage=DimensionScore(5, "s"),
            specificity=DimensionScore(5, "s"),
            correctness=DimensionScore(5, "s"),
            completeness=DimensionScore(4, "s"),
        )


@pytest.mark.asyncio
async def test_runner_writes_outputs_and_report(
    repo_root: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Runner should persist tmp outputs and docs report."""

    monkeypatch.delenv("BENCHMARK_TMP_DIR", raising=False)
    monkeypatch.delenv("BENCHMARK_DOCS_DIR", raising=False)
    config = BenchmarkConfig(
        _env_file=None,
        tmp_dir=tmp_path / "tmp",
        docs_dir=tmp_path / "docs",
    )
    runner = BenchmarkRunner(
        config,
        repo_root=repo_root,
        generator=_StubGenerator(),
        scorer=_StubScorer(),
    )

    comparison = await runner.run("issue-workflow", "issue-creation")

    assert comparison.delta == 9
    assert comparison.verdict == "significant improvement"
    assert (tmp_path / "tmp" / "issue-workflow" / "output-baseline.md").is_file()
    assert (tmp_path / "tmp" / "issue-workflow" / "output-with-skill.md").is_file()
    report_path = tmp_path / "docs" / "issue-workflow" / "report.md"
    assert report_path.is_file()
    assert "issue-workflow" in report_path.read_text(encoding="utf-8")


@pytest.fixture
def repo_root() -> Path:
    from skill_benchmark.paths import find_repo_root

    return find_repo_root()
