"""Validate baseline artifacts without selecting controls or assessing risk."""
from __future__ import annotations

import argparse
import json
from importlib.resources import files
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from . import (controls_bytes, mappings_bytes, applicability_taxonomy_bytes,
               agent_baseline_crosswalk_bytes)


class LibraryValidationError(ValueError):
    """An artifact violates its schema or cross-artifact references."""


def schema_document() -> dict:
    resource = files("ai_governance_control_framework").joinpath("schemas", "library.schema.json")
    try:
        return json.loads(resource.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return json.loads((Path(__file__).resolve().parents[2] / "schemas/library.schema.json").read_text())


def validate_schema(document: dict, kind: str) -> None:
    schema = schema_document()
    schema["$ref"] = f"#/$defs/{kind}"
    error = next(Draft202012Validator(schema).iter_errors(document), None)
    if error:
        location = ".".join(str(part) for part in error.absolute_path) or "root"
        raise LibraryValidationError(f"{kind}.{location}: {error.message}")


def validate_artifacts(controls: dict, mappings: dict, taxonomy: dict, crosswalk: dict) -> None:
    """Check structure, taxonomy membership, uniqueness, and traceability."""
    for kind, document in (("controls", controls), ("mappings", mappings),
                           ("taxonomy", taxonomy), ("crosswalk", crosswalk)):
        validate_schema(document, kind)
    records = controls["controls"]
    ids = [item["control_id"] for item in records]
    if len(ids) != len(set(ids)):
        raise LibraryValidationError("Duplicate control IDs")
    references = set(controls["reference_catalog"])
    for control in records:
        metadata = control["applicability_metadata"]
        if not set(control["references"]) <= references:
            raise LibraryValidationError(f"{control['control_id']}: unknown reference")
        if not set(metadata["contexts"]) <= set(taxonomy["object_types"]):
            raise LibraryValidationError(f"{control['control_id']}: unknown context")
        groups = metadata["trigger_conditions"]
        if bool(groups) != (metadata["mode"] == "conditional"):
            raise LibraryValidationError(f"{control['control_id']}: mode and triggers disagree")
        fields = {condition["field"] for group in groups for condition in group["all"]}
        if fields != set(metadata["required_inputs"]):
            raise LibraryValidationError(f"{control['control_id']}: required inputs disagree with triggers")
        if any(condition["operator"] not in taxonomy["condition_operators"]
               for group in groups for condition in group["all"]):
            raise LibraryValidationError(f"{control['control_id']}: unsupported operator")
    seen = set()
    for mapping in mappings["mappings"]:
        if mapping["control_id"] not in ids:
            raise LibraryValidationError("Mapping references unknown control")
        key = tuple(mapping[field] for field in ("control_id", "framework", "edition", "reference"))
        if key in seen:
            raise LibraryValidationError("Duplicate mapping")
        seen.add(key)
    source_ids = []
    for mapping in crosswalk["mappings"]:
        source_ids.append(mapping["source_control"])
        if not set(mapping["canonical_controls"]) <= set(ids):
            raise LibraryValidationError("Crosswalk references unknown canonical control")
    if len(source_ids) != len(set(source_ids)):
        raise LibraryValidationError("Duplicate crosswalk source control")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, help="Artifact data directory; defaults to installed package")
    args = parser.parse_args()
    readers = (controls_bytes, mappings_bytes, applicability_taxonomy_bytes, agent_baseline_crosswalk_bytes)
    names = ("controls.yaml", "mappings.yaml", "applicability-taxonomy.yaml", "agent-baseline-crosswalk.yaml")
    documents = [yaml.safe_load((args.directory / name).read_bytes() if args.directory else reader())
                 for name, reader in zip(names, readers)]
    validate_artifacts(*documents)
    print(f"Validated {len(documents[0]['controls'])} controls and their supporting artifacts")


if __name__ == "__main__":
    main()
