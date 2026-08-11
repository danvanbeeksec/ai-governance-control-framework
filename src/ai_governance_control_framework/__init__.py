"""Read-only access to the packaged AI governance control library."""

from __future__ import annotations

from importlib.resources import files
from pathlib import Path


__version__ = "0.1.0"


def controls_bytes() -> bytes:
    """Return the authoritative controls artifact exactly as packaged."""
    packaged = files(__package__).joinpath("resources", "controls.yaml")
    try:
        return packaged.read_bytes()
    except FileNotFoundError:
        source_checkout = Path(__file__).resolve().parents[2] / "data" / "controls.yaml"
        return source_checkout.read_bytes()


def controls_text() -> str:
    """Return the authoritative controls artifact as UTF-8 text."""
    return controls_bytes().decode("utf-8")
