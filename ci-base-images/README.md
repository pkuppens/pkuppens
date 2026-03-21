# CI Base Images

Shared Docker base images for faster CI across pkuppens projects. Pushed to `ghcr.io/pkuppens/pkuppens/`.

> **GHCR package README:** The package page on ghcr.io inherits the README from its connected repository. To show a purpose-focused README instead of the profile README: (1) create repo `pkuppens/ci-base-images`, (2) use `README.ghcr.md` as its root `README.md`, (3) connect each container package to that repo (Package settings → Connect repository).

## Images

| Image | Base | Contents | Typical Use |
|-------|------|----------|-------------|
| **ci-base-3.12** | python:3.12-slim | `build-essential`, uv, pytest, ruff, bandit, safety, pytest-cov | Lint, security, `uv sync` with native wheels |
| **ci-hf-base-3.12** | ci-base-3.12 | + HuggingFace env + models; **toolchain purged** after build | RAG, embedding tests |
| **ci-whisper-3.12** | ci-base-3.12 | + faster-whisper + model; **toolchain purged** after build | STT/voice pipelines |

ci-hf-base and ci-whisper are **siblings** (both FROM ci-base-3.12). Text tokenization differs from speech-to-text; stacking Whisper on HF would mix concerns.

## Benefits

- **Speed**: No model download per run; HF models and base tooling are baked in
- **Consistency**: Same Python/uv/tool versions across projects
- **Reduced runner load**: Less disk I/O and network per job

## Considerations

- **Build toolchain policy**: `ci-base-3.12` includes `build-essential` so dependent projects can compile native extensions during `uv sync`. **ci-hf-base-3.12** and **ci-whisper-3.12** run an explicit `apt-get purge` of that toolchain after Python installs and model download, to free space for large caches (HF / Whisper). Rebuild all three images after changing this policy.
- **Image size**: ci-hf-base ~2GB; ci-whisper ~1.5GB
- **Rebuild cadence**: Monthly (schedule) or manual (workflow_dispatch)
- **ghcr.io access**: Requires `packages: write` for the build workflow. Validate with a manual run of Build CI Base Images.
- **github.io**: Considered separately for deployments; document if/when used.

## Version Matrix

| Component | Version |
|-----------|---------|
| Python | 3.12 |
| uv | latest (pip) |
| pytest | >=7.4 |
| ruff | >=0.11 |
| bandit | >=1.7 |
| safety | >=2.0 |
| sentence-transformers | >=2.2 |
| faster-whisper | >=1.2 |

## Usage

In a consuming project (e.g. on_prem_rag):

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/pkuppens/pkuppens/ci-hf-base-3.12:latest
    steps:
      - uses: actions/checkout@v6
      - run: uv sync --dev
      - run: uv run pytest ...
```

## How-to: Combining HF and Whisper

When a project needs both HuggingFace embeddings and Whisper STT, build a custom image or use multi-stage:

```dockerfile
# Option A: FROM ci-hf-base, add Whisper
FROM ghcr.io/pkuppens/pkuppens/ci-hf-base-3.12:latest
RUN uv pip install --system faster-whisper
# ... download Whisper model

# Option B: Multi-stage, merge caches
# Build from ci-hf and ci-whisper, merge /opt/hf_cache if needed
```

This is not a delivered image; adapt to your project.

## TTS Note

Whisper STT pipelines may include TTS (text-to-speech). TTS is often client-side. Document in your project whether TTS runs server-side or client-side.

## ghcr.io Validation

1. Go to Actions → Build CI Base Images → Run workflow
2. If push succeeds, ghcr.io access is OK
3. If it fails, check repository Settings → Actions → General → Workflow permissions ("Read and write")
4. Ensure no IP/registry blocklists apply

## Build Locally

```bash
# From pkuppens/pkuppens repo root
docker build -f ci-base-images/Dockerfile.ci-base-3.12 -t ci-base-3.12:local .
# After pushing ci-base, build ci-hf (depends on ci-base-3.12:latest in registry)
docker build -f ci-base-images/Dockerfile.ci-hf-base-3.12 -t ci-hf-base-3.12:local .
```
