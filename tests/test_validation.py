from copy import deepcopy
from pathlib import Path
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ai_governance_control_framework.validation import LibraryValidationError, validate_artifacts


def artifacts():
    return [yaml.safe_load((ROOT / "data" / name).read_text()) for name in
            ("controls.yaml", "mappings.yaml", "applicability-taxonomy.yaml", "agent-baseline-crosswalk.yaml")]


def test_baseline_artifacts_validate():
    validate_artifacts(*artifacts())


@pytest.mark.parametrize("mutation", ["reference", "context", "operator", "input", "duplicate", "mapping"])
def test_invalid_derivatives_are_rejected(mutation):
    docs = deepcopy(artifacts())
    controls = docs[0]["controls"]
    conditional = next(c for c in controls if c["applicability_metadata"]["mode"] == "conditional")
    if mutation == "reference":
        controls[0]["references"] = ["UNKNOWN"]
    elif mutation == "context":
        controls[0]["applicability_metadata"]["contexts"] = ["unknown"]
    elif mutation == "operator":
        conditional["applicability_metadata"]["trigger_conditions"][0]["all"][0]["operator"] = "execute"
    elif mutation == "input":
        conditional["applicability_metadata"]["required_inputs"] = []
    elif mutation == "duplicate":
        controls.append(controls[0])
    else:
        docs[1]["mappings"][0]["control_id"] = "AI-UNKNOWN-001"
    with pytest.raises(LibraryValidationError):
        validate_artifacts(*docs)


def test_worked_example_uses_current_library_and_separate_assurance():
    example = yaml.safe_load((ROOT / "examples/sample-control-assessment.yaml").read_text())
    assert example["assessment"]["framework_version"] == artifacts()[0]["library"]["version"]
    for control in example["assessment"]["controls"]:
        assert control["assurance_state"] == "not_tested"
        assert "implementation_state" in control
