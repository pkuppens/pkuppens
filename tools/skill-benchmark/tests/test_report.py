from skill_benchmark.models import BenchmarkComparison, DimensionScore, ScoringResult, TaskPrompt
from skill_benchmark.report import ReportGenerator


def _sample_comparison(delta: int = 5) -> BenchmarkComparison:
    """Build a comparison with the requested total score delta."""

    baseline = ScoringResult(
        coverage=DimensionScore(2, "baseline coverage"),
        specificity=DimensionScore(2, "baseline specificity"),
        correctness=DimensionScore(3, "baseline correctness"),
        completeness=DimensionScore(3, "baseline completeness"),
    )
    skilled_total = baseline.total + delta
    skilled_scores = _scores_for_total(skilled_total)
    skilled = ScoringResult(
        coverage=DimensionScore(skilled_scores[0], "skilled coverage"),
        specificity=DimensionScore(skilled_scores[1], "skilled specificity"),
        correctness=DimensionScore(skilled_scores[2], "skilled correctness"),
        completeness=DimensionScore(skilled_scores[3], "skilled completeness"),
    )
    return BenchmarkComparison(
        task=TaskPrompt(name="issue-creation", prompt="Create issue", expected_coverage="criteria"),
        skill_name="issue-workflow",
        baseline_output="baseline",
        skilled_output="skilled",
        baseline_score=baseline,
        skilled_score=skilled,
    )


def _scores_for_total(total: int) -> tuple[int, int, int, int]:
    """Split a total score across four 1-5 dimensions."""

    remaining = max(4, min(20, total))
    scores = [1, 1, 1, 1]
    idx = 0
    while remaining > 4:
        if scores[idx] < 5:
            scores[idx] += 1
            remaining -= 1
        idx = (idx + 1) % 4
    return scores[0], scores[1], scores[2], scores[3]


def test_report_contains_scoring_table_and_verdict() -> None:
    """Report markdown should include table, totals, and verdict."""

    report = ReportGenerator().generate(_sample_comparison())
    assert "## Scoring (1–5 per dimension)" in report
    assert "| Coverage |" in report
    assert "**Total**" in report
    assert "## Verdict" in report
    assert "Significant Improvement" in report or "significant improvement" in report.lower()


def test_verdict_marginal_and_no_improvement() -> None:
    """Verdict labels should follow delta thresholds."""

    marginal = _sample_comparison(delta=2)
    assert marginal.verdict == "marginal"

    none = _sample_comparison(delta=0)
    assert none.verdict == "no improvement"


def test_report_save_writes_file(tmp_path) -> None:
    """ReportGenerator.save should create report.md under skill directory."""

    report = ReportGenerator().generate(_sample_comparison())
    path = ReportGenerator().save(report, "issue-workflow", tmp_path)
    assert path == tmp_path / "issue-workflow" / "report.md"
    assert path.read_text(encoding="utf-8") == report
