import hashlib
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_governance_control_framework import (
    __version__, applicability_taxonomy_bytes, controls_bytes, mappings_bytes,
)


def test_package_exposes_exact_authoritative_artifact():
    authoritative = (ROOT / "data" / "controls.yaml").read_bytes()

    assert controls_bytes() == authoritative
    assert hashlib.sha256(controls_bytes()).hexdigest() == (
        "c0cef3a0046aa74b1705382d56a8d4659f86d119e7635dfefe8804d6e51d0fe2"
    )
    assert __version__ == "1.1.0"

    assert mappings_bytes() == (ROOT / "data" / "mappings.yaml").read_bytes()
    assert applicability_taxonomy_bytes() == (
        ROOT / "data" / "applicability-taxonomy.yaml"
    ).read_bytes()
