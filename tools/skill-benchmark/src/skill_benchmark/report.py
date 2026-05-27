"""Markdown report generation for benchmark comparisons."""

from __future__ import annotations

from pathlib import Path

from .models import BenchmarkComparison, ScoringResult


class ReportGenerator:
    """Render and persist benchmark comparison reports."""

    def generate(self, comparison: BenchmarkComparison) -> str:
        """Build a markdown report for one benchmark run.

        Args:
            comparison (BenchmarkComparison): Baseline vs with-skill comparison.

        Returns:
            str: Markdown report body.
        """

        task = comparison.task
        baseline = comparison.baseline_score
        skilled = comparison.skilled_score

        lines = [
            f"# Skill Benchmark — {comparison.skill_name}",
            "",
            f"**Task:** {task.name}",
            "",
            "## Task prompt",
            "",
            task.prompt,
            "",
            "## Scoring (1–5 per dimension)",
            "",
            "| Dimension | Without Skill | With Skill | Delta |",
            "|-----------|---------------|------------|-------|",
            _score_row("Coverage", baseline.coverage.score, skilled.coverage.score),
            _score_row("Specificity", baseline.specificity.score, skilled.specificity.score),
            _score_row("Correctness", baseline.correctness.score, skilled.correctness.score),
            _score_row("Completeness", baseline.completeness.score, skilled.completeness.score),
            (
                f"| **Total** | **{baseline.total}/20** | **{skilled.total}/20** | "
                f"**{comparison.delta:+d}** |"
            ),
            "",
            "## Verdict",
            "",
            f"**{comparison.verdict.title()}** — delta {comparison.delta:+d} "
            f"({baseline.total}/20 → {skilled.total}/20).",
            "",
            "## Key observation",
            "",
            _key_observation(comparison),
            "",
            "## Scoring rationale",
            "",
            "### Without skill",
            "",
            _rationale_block(baseline),
            "",
            "### With skill",
            "",
            _rationale_block(skilled),
        ]
        return "\n".join(lines)

    def save(self, report: str, skill_name: str, docs_dir: Path) -> Path:
        """Write a report to docs/skills/benchmark/<skill>/report.md.

        Args:
            report (str): Markdown report body.
            skill_name (str): Skill directory name.
            docs_dir (Path): Base docs output directory (repo-relative resolved).

        Returns:
            Path: Path to the written report file.
        """

        output_dir = docs_dir / skill_name
        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / "report.md"
        report_path.write_text(report, encoding="utf-8")
        return report_path


def _score_row(label: str, baseline: int, skilled: int, *, bold: bool = False) -> str:
    """Format one scoring table row."""

    delta = skilled - baseline
    name = label if not bold else label
    return f"| {name} | {baseline}/5 | {skilled}/5 | {delta:+d} |"


def _rationale_block(result: ScoringResult) -> str:
    """Format dimension rationales as bullet list."""

    return "\n".join(
        [
            f"- **Coverage ({result.coverage.score}/5):** {result.coverage.rationale}",
            f"- **Specificity ({result.specificity.score}/5):** {result.specificity.rationale}",
            f"- **Correctness ({result.correctness.score}/5):** {result.correctness.rationale}",
            f"- **Completeness ({result.completeness.score}/5):** {result.completeness.rationale}",
        ]
    )


def _key_observation(comparison: BenchmarkComparison) -> str:
    """Summarize the largest scoring delta dimension."""

    deltas = {
        "coverage": comparison.skilled_score.coverage.score
        - comparison.baseline_score.coverage.score,
        "specificity": comparison.skilled_score.specificity.score
        - comparison.baseline_score.specificity.score,
        "correctness": comparison.skilled_score.correctness.score
        - comparison.baseline_score.correctness.score,
        "completeness": comparison.skilled_score.completeness.score
        - comparison.baseline_score.completeness.score,
    }
    best_dim = max(deltas, key=deltas.get)
    return (
        f"Largest gain in **{best_dim}** ({deltas[best_dim]:+d}). "
        f"Overall verdict: {comparison.verdict}."
    )
