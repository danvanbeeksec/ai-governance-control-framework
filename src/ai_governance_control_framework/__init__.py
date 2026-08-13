"""Read-only access to the packaged AI governance control library."""

from __future__ import annotations

from importlib.resources import files
from pathlib import Path


__version__ = "1.1.0"


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


def mappings_bytes() -> bytes:
    """Return the optional high-confidence mapping artifact exactly as packaged."""
    packaged = files(__package__).joinpath("resources", "mappings.yaml")
    try:
        return packaged.read_bytes()
    except FileNotFoundError:
        source_checkout = Path(__file__).resolve().parents[2] / "data" / "mappings.yaml"
        return source_checkout.read_bytes()


def mappings_text() -> str:
    """Return the mapping artifact as UTF-8 text."""
    return mappings_bytes().decode("utf-8")


def applicability_taxonomy_bytes() -> bytes:
    """Return the structured applicability taxonomy exactly as packaged."""
    packaged = files(__package__).joinpath("resources", "applicability-taxonomy.yaml")
    try:
        return packaged.read_bytes()
    except FileNotFoundError:
        source_checkout = (
            Path(__file__).resolve().parents[2] / "data" / "applicability-taxonomy.yaml"
        )
        return source_checkout.read_bytes()
