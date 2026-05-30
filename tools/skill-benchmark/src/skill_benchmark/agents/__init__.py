"""LLM agents for the skill benchmark harness.

This package holds the two model-backed steps in a benchmark run:

1. **Generator** — produces task output with and without skill context.
2. **Scorer** — rates each output on coverage, specificity, correctness, and
   completeness.

Both agents use :class:`~skill_benchmark.provider.LLMProvider` and are wired
by :class:`~skill_benchmark.runner.BenchmarkRunner`. See
``skills/validation/skill-benchmark/SKILL.md`` for the manual benchmark
workflow this harness automates.

Exports
-------
GeneratorAgent
    Baseline and with-skill generation for one task prompt.
ScorerAgent
    Independent rubric scoring for one generated output.

Example
-------
Inject agents in tests or call via the runner::

    from skill_benchmark.agents import GeneratorAgent, ScorerAgent
    from skill_benchmark.config import BenchmarkConfig
    from skill_benchmark.provider import LLMProvider

    config = BenchmarkConfig()
    generator = GeneratorAgent(LLMProvider(config))
    scorer = ScorerAgent(config)

    # Typical use is through BenchmarkRunner.run(skill_name, task_name).
"""

from .generator import GeneratorAgent
from .scorer import ScorerAgent

__all__ = ["GeneratorAgent", "ScorerAgent"]
