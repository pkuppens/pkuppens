---
name: deployment-build
description: Builds artefacts (container images, packages, bundles) and validates build pipeline output. Use when preparing a release, running docker build, uv build, or a CI build job, or when verifying artefact integrity before release.
---

# Deployment Build

Builds release artefacts and validates build pipeline output before release.

**When to use:**
- Before releasing to staging or production
- After a feature branch is merged to main
- When running `docker build`, `uv build`, or a CI build workflow manually
- When verifying that artefacts are reproducible and pass integrity checks

**Instructions:**

1. **Identify artefact type** — container image, Python wheel/sdist, static bundle, or binary
2. **Run build command** (repo-specific):
   - Container: `docker build -t <image>:<tag> .` or `docker compose build`
   - Python: `uv build` (produces `dist/`)
   - Node: `npm run build` or `vite build`
   - CI: `gh workflow run build.yml`
3. **Validate artefact**:
   - Container: `docker run --rm <image>:<tag> <healthcheck-cmd>`
   - Python: `uv pip install dist/*.whl --dry-run` or smoke test
   - Check image size, layer count (flag unexpectedly large images)
4. **Tag and label**:
   - Tag with semantic version: `<image>:<semver>` and `<image>:latest`
   - Include build metadata: git SHA, branch, timestamp
5. **Check build reproducibility** — run build twice, compare checksums where feasible
6. **Record artefact reference** in `tmp/deployment/build-<version>.md`:
   - Image digest or wheel hash
   - Build timestamp
   - CI run URL (if applicable)

**Output format:**

```
## Build Summary
- Artefact: <type> — <name>:<version>
- Digest/hash: <value>
- Build command: <cmd>
- Status: ✅ success / ❌ failed
- Notes: <any warnings or anomalies>
```

**Integration:** Follows `integration-merge`. Precedes `deployment-release`. See COOPERATION.md.
