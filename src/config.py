"""Shared settings so every notebook uses the same seed and paths."""

from pathlib import Path

SEED = 2027

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "reports" / "figures"
