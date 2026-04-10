---
name: skill-benchmark
description: Evaluates skill effectiveness by comparing agent output on a task with and without skills activated. Use when validating that a skill improves output quality, when creating evidence for a skill PR, or when regression-testing skill changes.
---

# Skill Benchmark

Measures the real-world impact of a skill by comparing agent output with and without skill activation.

**When to use:**
- Validating that a new or revised skill improves output quality
- Creating evidence for a skill-related pull request or issue
- Regression-testing a skill after edits
- Demonstrating AI skill value to stakeholders

**Instructions:**

1. **Select a benchmark task**:
   - Choose a concrete, reproducible task relevant to the skill under test
   - Example tasks:
     - Create a GitHub issue for adding BM25 retrieval to `on_prem_rag`
     - Write an ADR for choosing FastAPI over Flask
     - Produce a deployment checklist for `on_prem_rag` 0.9.0
   - Record the task prompt in `tmp/skills/benchmark/<skill-name>/task.md`

2. **Run baseline (without skill)**:
   - Invoke the agent with the task prompt only — no skill context
   - Save the full output to `tmp/skills/benchmark/<skill-name>/output-baseline.md`
   - Do NOT provide any skill text, examples, or hints

3. **Run with skill activated**:
   - Invoke the agent with the task prompt + skill name/trigger
   - Save the full output to `tmp/skills/benchmark/<skill-name>/output-with-skill.md`

4. **Score both outputs** on 4 dimensions (1–5 scale each):

   | Dimension | Description |
   |-----------|-------------|
   | Coverage | Did the output address all required sub-tasks? |
   | Specificity | Are commands, formats, and values concrete (not vague)? |
   | Correctness | Is the output factually and technically correct? |
   | Completeness | Could an engineer act on this output without further clarification? |

5. **Produce comparison table**:

   | Dimension | Without Skill | With Skill | Delta |
   |-----------|--------------|------------|-------|
   | Coverage | /5 | /5 | +N |
   | Specificity | /5 | /5 | +N |
   | Correctness | /5 | /5 | +N |
   | Completeness | /5 | /5 | +N |
   | **Total** | **/20** | **/20** | **+N** |

6. **Write benchmark report** in `tmp/skills/benchmark/<skill-name>/report.md`:
   - Task prompt used
   - Scoring rationale for each dimension
   - Key qualitative differences (specific examples from outputs)
   - Verdict: skill improves output (delta ≥ +4) / marginal / no measurable improvement

**Output format:**

```
## Skill Benchmark — <skill-name>
- Task: <one-line description>
- Without skill total: <N>/20
- With skill total: <N>/20
- Delta: +<N>
- Verdict: significant improvement | marginal | no improvement
- Key observation: <one sentence on the most important qualitative difference>
```

**Benchmark task library:** Reusable prompts live under **`docs/skills/benchmark/tasks/`** in this repo (versioned). Local copies may also sit in `tmp/skills/benchmark/tasks/` during runs.

- `issue-creation.md` — create a GitHub issue for a feature
- `adr-authoring.md` — write an ADR for a technology choice
- `deployment-checklist.md` — produce a deployment checklist for a release

**Committed reports** (examples / evidence): `docs/skills/benchmark/<skill-name>/report.md`. Session transcripts can remain in `tmp/skills/benchmark/<skill-name>/`.

**Anti-patterns:**
- Using the same session for both runs (context contamination)
- Choosing tasks where the skill is explicitly referenced in the prompt
- Scoring on style rather than actionability

**Integration:** Output feeds `architecture-risks-debt` if skills have known gaps. Store runnable evidence under `docs/skills/benchmark/` (or `tmp/skills/benchmark/` for scratch). See COOPERATION.md.
