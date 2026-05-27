"""End-to-end benchmark orchestration."""

from __future__ import annotations

from pathlib import Path

from .agents.generator import GeneratorAgent
from .agents.scorer import ScorerAgent
from .config import BenchmarkConfig
from .loader import SkillLoader, TaskLoader
from .models import BenchmarkComparison
from .paths import find_repo_root
from .provider import LLMProvider
from .report import ReportGenerator


class BenchmarkRunner:
    """Run a full baseline vs with-skill benchmark pipeline."""

    def __init__(
        self,
        config: BenchmarkConfig,
        *,
        repo_root: Path | None = None,
        generator: GeneratorAgent | None = None,
        scorer: ScorerAgent | None = None,
    ) -> None:
        """Create a runner with optional injected agents for tests.

        Args:
            config (BenchmarkConfig): Benchmark configuration.
            repo_root (Path | None): Repository root override.
            generator (GeneratorAgent | None): Optional generator for tests.
            scorer (ScorerAgent | None): Optional scorer for tests.
        """

        self._config = config
        self._repo_root = repo_root or find_repo_root()
        self._task_loader = TaskLoader(self._repo_root)
        self._skill_loader = SkillLoader(self._repo_root)
        self._generator = generator or GeneratorAgent(LLMProvider(config))
        self._scorer = scorer or ScorerAgent(config)
        self._reporter = ReportGenerator()

    @property
    def repo_root(self) -> Path:
        """Return the resolved repository root."""

        return self._repo_root

    def resolve_tmp_dir(self) -> Path:
        """Return absolute tmp output directory."""

        return self._resolve_path(self._config.tmp_dir)

    def resolve_docs_dir(self) -> Path:
        """Return absolute docs output directory."""

        return self._resolve_path(self._config.docs_dir)

    async def run(self, skill_name: str, task_name: str) -> BenchmarkComparison:
        """Execute one benchmark and write artefacts.

        Args:
            skill_name (str): Skill directory name under `skills/`.
            task_name (str): Task file stem under docs/skills/benchmark/tasks/.

        Returns:
            BenchmarkComparison: Structured comparison with scores and verdict.
        """

        task = self._task_loader.load(task_name)
        skill = self._skill_loader.load(skill_name)

        baseline = await self._generator.generate(task, skill=None)
        skilled = await self._generator.generate(task, skill=skill)

        baseline_score = await self._scorer.score(task, baseline.output)
        skilled_score = await self._scorer.score(task, skilled.output)

        comparison = BenchmarkComparison(
            task=task,
            skill_name=skill_name,
            baseline_output=baseline.output,
            skilled_output=skilled.output,
            baseline_score=baseline_score,
            skilled_score=skilled_score,
        )

        tmp_dir = self.resolve_tmp_dir() / skill_name
        tmp_dir.mkdir(parents=True, exist_ok=True)
        (tmp_dir / "output-baseline.md").write_text(baseline.output, encoding="utf-8")
        (tmp_dir / "output-with-skill.md").write_text(skilled.output, encoding="utf-8")

        report = self._reporter.generate(comparison)
        self._reporter.save(report, skill_name, self.resolve_docs_dir())

        return comparison

    def _resolve_path(self, configured: Path) -> Path:
        """Resolve repo-relative paths from the repository root."""

        if configured.is_absolute():
            return configured
        return (self._repo_root / configured).resolve()
