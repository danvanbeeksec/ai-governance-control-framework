import hashlib
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_governance_control_framework import __version__, controls_bytes


def test_package_exposes_exact_authoritative_artifact():
    authoritative = (ROOT / "data" / "controls.yaml").read_bytes()

    assert controls_bytes() == authoritative
    assert hashlib.sha256(controls_bytes()).hexdigest() == (
        "ba2c9b793fe239dbe63432fd6c0c06f1abf3b09b2ef5dafeafc7e10df330fc84"
    )
    assert __version__ == "0.1.0"
