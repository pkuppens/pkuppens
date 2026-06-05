#!/usr/bin/env python3
"""Pre-download HuggingFace models for ci-hf-base-3.12.

Matches on_prem_rag setup_embedding_models.py --ci models:
- sentence-transformers/all-MiniLM-L6-v2
- BAAI/bge-small-en-v1.5

Uses snapshot_download with pinned revisions and HF_TOKEN when set.
"""

from __future__ import annotations

import os
import sys
import time

try:
    from huggingface_hub import snapshot_download
    from sentence_transformers import SentenceTransformer
    from transformers import AutoModel, AutoTokenizer
except ImportError as exc:
    raise SystemExit(f"Required packages not installed: {exc}") from exc

# Pinned revisions (HF commit SHAs) for reproducible CI builds.
CI_MODELS: list[tuple[str, str]] = [
    ("sentence-transformers/all-MiniLM-L6-v2", "1110a243fdf4706b3f48f1d95db1a4f5529b4d41"),
    ("BAAI/bge-small-en-v1.5", "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"),
]

MAX_ATTEMPTS = 3
RETRY_SLEEP_SECONDS = 60


def _hf_token() -> str | None:
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    return token if token else None


def _setup_cache_dirs() -> str:
    hf_home = os.environ.get("HF_HOME", "/opt/hf_cache")
    transformers_cache = os.environ.get("TRANSFORMERS_CACHE", f"{hf_home}/hub")
    st_home = os.environ.get("SENTENCE_TRANSFORMERS_HOME", f"{hf_home}/sentence_transformers")

    os.makedirs(hf_home, exist_ok=True)
    os.makedirs(transformers_cache, exist_ok=True)
    os.makedirs(st_home, exist_ok=True)

    os.environ["HF_HOME"] = hf_home
    os.environ["TRANSFORMERS_CACHE"] = transformers_cache
    os.environ["SENTENCE_TRANSFORMERS_HOME"] = st_home
    return hf_home


def _download_models(cache_dir: str) -> list[str]:
    token = _hf_token()
    local_paths: list[str] = []

    for repo_id, revision in CI_MODELS:
        print(f"[Download] {repo_id} @ {revision[:12]}")
        local_path = snapshot_download(
            repo_id=repo_id,
            revision=revision,
            cache_dir=cache_dir,
            token=token,
        )
        local_paths.append(local_path)
        print(f"[OK] {repo_id} -> {local_path}")

    return local_paths


def _smoke_test(local_paths: list[str]) -> None:
    minilm_path, bge_path = local_paths

    print("[Smoke] SentenceTransformer load")
    model = SentenceTransformer(minilm_path, device="cpu")
    model.encode(["CI model cache smoke test"])

    print("[Smoke] BGE AutoModel + AutoTokenizer load")
    AutoModel.from_pretrained(bge_path)
    AutoTokenizer.from_pretrained(bge_path)


def main() -> None:
    """Download CI embedding models with retries."""
    cache_dir = _setup_cache_dirs()
    token = _hf_token()
    print(f"[Config] HF_TOKEN present: {bool(token)}")

    last_error: Exception | None = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            local_paths = _download_models(cache_dir)
            _smoke_test(local_paths)
            print("[OK] CI models downloaded and validated")
            return
        except Exception as exc:  # noqa: BLE001 — retry any hub/network failure
            last_error = exc
            if attempt >= MAX_ATTEMPTS:
                break
            sleep_for = RETRY_SLEEP_SECONDS * attempt
            print(f"[Retry] attempt {attempt}/{MAX_ATTEMPTS} failed: {exc}", file=sys.stderr)
            print(f"[Retry] sleeping {sleep_for}s before next attempt")
            time.sleep(sleep_for)

    raise SystemExit(f"Model download failed after {MAX_ATTEMPTS} attempts: {last_error}") from last_error


if __name__ == "__main__":
    main()
