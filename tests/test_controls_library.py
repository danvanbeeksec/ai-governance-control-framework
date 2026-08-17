from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTROL_FILE = ROOT / "data" / "controls.yaml"
MAPPING_FILE = ROOT / "data" / "mappings.yaml"
AGENT_BASELINE_CROSSWALK_FILE = ROOT / "data" / "agent-baseline-crosswalk.yaml"

REQUIRED_FIELDS = {
    "control_id",
    "domain",
    "layer",
    "title",
    "objective",
    "requirement",
    "applicability",
    "applicability_metadata",
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
    "usage_workforce",
    "inventory_lifecycle",
    "risk_impact_compliance",
    "systems_models_platforms",
    "human_oversight_transparency",
}


def load_library():
    with CONTROL_FILE.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def test_control_library_schema_and_unique_ids():
    library = load_library()
    controls = library["controls"]
    reference_keys = set(library["reference_catalog"])

    assert library["schema_version"] == "2.1"
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
        metadata = control["applicability_metadata"]
        assert metadata["contexts"]
        assert metadata["mode"] in {"universal", "conditional", "human_determination"}
        assert set(metadata) == {
            "contexts", "mode", "trigger_conditions", "required_inputs", "exclusions", "rationale"
        }
        assert metadata["rationale"].strip()
        trigger_fields = {
            condition["field"]
            for group in metadata["trigger_conditions"]
            for condition in group["all"]
        }
        assert set(metadata["required_inputs"]) == trigger_fields
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
    text = "\n".join(
        path.read_text(encoding="utf-8").lower()
        for path in (CONTROL_FILE, MAPPING_FILE)
    )
    prohibited_terms = ("marketaxess", "market axess")
    assert not any(term in text for term in prohibited_terms)


def test_mapping_library_is_optional_high_confidence_and_referentially_valid():
    controls = {control["control_id"] for control in load_library()["controls"]}
    with MAPPING_FILE.open(encoding="utf-8") as stream:
        mapping_library = yaml.safe_load(stream)

    assert mapping_library["schema_version"] == "1.0"
    mappings = mapping_library["mappings"]
    assert len(mappings) < len(controls)
    required = {
        "control_id", "framework", "edition", "reference", "category",
        "basis", "confidence", "rationale",
    }
    for mapping in mappings:
        assert required <= set(mapping)
        assert mapping["control_id"] in controls
        assert mapping["framework"] in {
            "ISO-IEC-27001", "ISO-IEC-42001", "EU-AI-ACT", "DORA", "SOC-2"
        }
        assert mapping["category"] in {"requirement", "guideline"}
        assert mapping["basis"] in {"source_supported", "inferred"}
        assert mapping["confidence"] == "high"
        assert mapping["reference"].strip()
        assert mapping["rationale"].strip()


def test_mappings_are_unique():
    with MAPPING_FILE.open(encoding="utf-8") as stream:
        mappings = yaml.safe_load(stream)["mappings"]
    keys = {
        (m["control_id"], m["framework"], m["edition"], m["reference"])
        for m in mappings
    }
    assert len(keys) == len(mappings)


def test_agent_baseline_crosswalk_is_complete_and_non_authoritative():
    controls = {control["control_id"] for control in load_library()["controls"]}
    with AGENT_BASELINE_CROSSWALK_FILE.open(encoding="utf-8") as stream:
        crosswalk = yaml.safe_load(stream)

    assert crosswalk["source"]["version"] == "1.0-draft"
    assert crosswalk["source"]["status"] == "draft"
    assert crosswalk["interpretation"]["authority"] == "data/controls.yaml remains the sole control authority."
    mappings = crosswalk["mappings"]
    assert len(mappings) == 35
    assert len({mapping["source_control"] for mapping in mappings}) == 35
    assert all(mapping["coverage"] == "normalized" for mapping in mappings)
    assert all(set(mapping["canonical_controls"]) <= controls for mapping in mappings)


def test_human_readable_catalog_is_current():
    result = subprocess.run(
        [sys.executable, ROOT / "scripts" / "render_control_catalog.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout

    result = subprocess.run(
        [sys.executable, ROOT / "scripts" / "render_mapping_catalog.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout
