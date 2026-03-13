# CI Base Images for GitHub Actions

Starter Docker images for fast, consistent Python CI in GitHub Actions. Pre-installed tooling and models reduce setup time and network load on each run.

## Images

| Image | Purpose | Includes |
|-------|---------|----------|
| **ci-base-3.12** | General Python CI | Python 3.12, uv, pytest, ruff, bandit, safety, pytest-cov |
| **ci-hf-base-3.12** | RAG / embeddings | ci-base + HuggingFace, sentence-transformers, pre-downloaded models (all-MiniLM-L6-v2, bge-small-en-v1.5) |
| **ci-whisper-3.12** | Speech-to-text | ci-base + faster-whisper, pre-downloaded Whisper base model |

## Quick start

Add this to your GitHub Actions workflow:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/pkuppens/pkuppens/ci-base-3.12:latest
    steps:
      - uses: actions/checkout@v6
      - run: uv sync --dev
      - run: uv run pytest
      - run: uv run ruff check .
      - run: uv run bandit -r src/
```

For embedding or RAG tests, use `ci-hf-base-3.12:latest`; for speech-to-text, use `ci-whisper-3.12:latest`.

## Why use these images?

- **Speed** – No per-run model or tool downloads; everything is baked in.
- **Consistency** – Same Python, uv, and tool versions across projects.
- **Less runner load** – Smaller layers and fewer network calls.

## Full documentation

Source, build instructions, version matrix, and advanced usage: [pkuppens/pkuppens – ci-base-images](https://github.com/pkuppens/pkuppens/tree/main/ci-base-images)

---

*Maintained by [pkuppens](https://github.com/pkuppens).*
