from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTROL_FILE = ROOT / "data" / "controls.yaml"

REQUIRED_FIELDS = {
    "control_id",
    "domain",
    "layer",
    "title",
    "objective",
    "requirement",
    "applicability",
    "evidence_examples",
    "implementation_notes",
    "references",
}

EXPECTED_DOMAINS = {
    "administrative_governance",
    "technical_security",
    "data_privacy",
    "lifecycle",
    "agentic_ai",
    "monitoring_operations",
    "vendor_supply_chain",
}


def load_library():
    with CONTROL_FILE.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def test_control_library_schema_and_unique_ids():
    library = load_library()
    controls = library["controls"]
    reference_keys = set(library["reference_catalog"])

    assert library["schema_version"] == "1.0"
    assert controls
    assert len({control["control_id"] for control in controls}) == len(controls)

    for control in controls:
        assert REQUIRED_FIELDS == set(control)
        assert control["domain"] in EXPECTED_DOMAINS
        assert control["layer"] in {"enterprise", "ai_system", "both"}
        assert control["control_id"].startswith("AI-")
        assert control["objective"].strip()
        assert control["requirement"].strip()
        assert control["applicability"].strip()
        assert control["evidence_examples"]
        assert control["implementation_notes"].strip()
        assert set(control["references"]) <= reference_keys


def test_all_framework_domains_are_represented():
    controls = load_library()["controls"]
    assert {control["domain"] for control in controls} == EXPECTED_DOMAINS


def test_both_control_layers_are_represented():
    controls = load_library()["controls"]
    layers = {control["layer"] for control in controls}
    assert {"enterprise", "ai_system"} <= layers


def test_library_contains_no_company_specific_reference():
    text = CONTROL_FILE.read_text(encoding="utf-8").lower()
    prohibited_terms = ("marketaxess", "market axess")
    assert not any(term in text for term in prohibited_terms)


def test_human_readable_catalog_is_current():
    result = subprocess.run(
        [sys.executable, ROOT / "scripts" / "render_control_catalog.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout
