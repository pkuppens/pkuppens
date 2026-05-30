"""Data models shared across loaders, agents, runner, and report.

Includes task and skill inputs, generation and scoring results, and the
aggregate :class:`BenchmarkComparison` used for report generation.

Deliverable: typed dataclasses passed between benchmark pipeline stages.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TaskPrompt:
    """A benchmark task loaded from docs/skills/benchmark/tasks/."""

    name: str
    prompt: str
    expected_coverage: str
    skill_under_test: str | None = None


@dataclass(frozen=True)
class SkillContent:
    """Skill markdown content loaded from skills/<name>/SKILL.md."""

    name: str
    content: str


@dataclass(frozen=True)
class GenerationResult:
    """Output from a single LLM generation call."""

    output: str
    model: str
    input_tokens: int | None = None
    output_tokens: int | None = None


@dataclass(frozen=True)
class DimensionScore:
    """Score for one rubric dimension with rationale."""

    score: int
    rationale: str


@dataclass(frozen=True)
class ScoringResult:
    """Four-dimension scoring result (total out of 20)."""

    coverage: DimensionScore
    specificity: DimensionScore
    correctness: DimensionScore
    completeness: DimensionScore

    @property
    def total(self) -> int:
        """Return the sum of all dimension scores."""

        return (
            self.coverage.score
            + self.specificity.score
            + self.correctness.score
            + self.completeness.score
        )


@dataclass(frozen=True)
class BenchmarkComparison:
    """Baseline vs with-skill comparison for one task."""

    task: TaskPrompt
    skill_name: str
    baseline_output: str
    skilled_output: str
    baseline_score: ScoringResult
    skilled_score: ScoringResult

    @property
    def delta(self) -> int:
        """Return skilled total minus baseline total."""

        return self.skilled_score.total - self.baseline_score.total

    @property
    def verdict(self) -> str:
        """Return a human-readable verdict label."""

        if self.delta >= 4:
            return "significant improvement"
        if self.delta >= 1:
            return "marginal"
        return "no improvement"
