#!/usr/bin/env python3
"""Pre-download HuggingFace models for ci-hf-base-3.12.

Matches on_prem_rag setup_embedding_models.py --ci models:
- sentence-transformers/all-MiniLM-L6-v2
- BAAI/bge-small-en-v1.5

Run with: python download_hf_ci_models.py
Environment: HF_HOME, TRANSFORMERS_CACHE, SENTENCE_TRANSFORMERS_HOME must be set.
"""

from __future__ import annotations

import os

# Minimal imports to avoid pulling full llama-index etc.
try:
    from sentence_transformers import SentenceTransformer
    from transformers import AutoModel, AutoTokenizer
except ImportError as e:
    raise SystemExit(f"Required packages not installed: {e}") from e


def main() -> None:
    """Download CI embedding models."""
    hf_home = os.environ.get("HF_HOME", "/opt/hf_cache")
    transformers_cache = os.environ.get("TRANSFORMERS_CACHE", f"{hf_home}/hub")
    st_home = os.environ.get("SENTENCE_TRANSFORMERS_HOME", f"{hf_home}/sentence_transformers")

    os.makedirs(hf_home, exist_ok=True)
    os.makedirs(transformers_cache, exist_ok=True)
    os.makedirs(st_home, exist_ok=True)

    os.environ["HF_HOME"] = hf_home
    os.environ["TRANSFORMERS_CACHE"] = transformers_cache
    os.environ["SENTENCE_TRANSFORMERS_HOME"] = st_home

    # sentence-transformers
    print("[Download] sentence-transformers/all-MiniLM-L6-v2")
    SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")

    # transformers (bge-small)
    print("[Download] BAAI/bge-small-en-v1.5")
    AutoModel.from_pretrained("BAAI/bge-small-en-v1.5")
    AutoTokenizer.from_pretrained("BAAI/bge-small-en-v1.5")

    print("[OK] CI models downloaded")


if __name__ == "__main__":
    main()
