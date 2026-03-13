#!/usr/bin/env python3
"""Pre-download Whisper base model for ci-whisper-3.12."""
from faster_whisper import WhisperModel

WhisperModel("base", device="cpu", compute_type="int8")
print("[OK] Whisper base model downloaded")
