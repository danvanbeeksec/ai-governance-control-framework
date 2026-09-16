import hashlib
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_governance_control_framework import (
    __version__, agent_baseline_crosswalk_bytes, applicability_taxonomy_bytes,
    controls_bytes, mappings_bytes,
)


def test_package_exposes_exact_authoritative_artifact():
    authoritative = (ROOT / "data" / "controls.yaml").read_bytes()

    assert controls_bytes() == authoritative
    assert hashlib.sha256(controls_bytes()).hexdigest() == (
        "e01c880933b3385f6b8a490f867cd5d2627a97134eaad8fced2a15d4831eb510"
    )
    assert __version__ == "1.2.0"

    assert mappings_bytes() == (ROOT / "data" / "mappings.yaml").read_bytes()
    assert applicability_taxonomy_bytes() == (
        ROOT / "data" / "applicability-taxonomy.yaml"
    ).read_bytes()
    assert agent_baseline_crosswalk_bytes() == (
        ROOT / "data" / "agent-baseline-crosswalk.yaml"
    ).read_bytes()
