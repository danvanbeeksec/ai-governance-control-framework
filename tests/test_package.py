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
        "dd7f696df558302808e71a0fab74153f815b86fa923335806a791146d78fdcc6"
    )
    assert __version__ == "1.2.0"

    assert mappings_bytes() == (ROOT / "data" / "mappings.yaml").read_bytes()
    assert applicability_taxonomy_bytes() == (
        ROOT / "data" / "applicability-taxonomy.yaml"
    ).read_bytes()
    assert agent_baseline_crosswalk_bytes() == (
        ROOT / "data" / "agent-baseline-crosswalk.yaml"
    ).read_bytes()
