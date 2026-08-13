"""Render high-confidence framework mappings as Markdown."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "mappings.yaml"
OUTPUT = ROOT / "mappings" / "control-reference-mapping.md"


def render(mapping_library: dict) -> str:
    mappings = mapping_library["mappings"]
    lines = [
        "<!-- Generated from data/mappings.yaml. Do not edit directly. -->",
        "# High-Confidence Framework Mappings",
        "",
        "## Interpretation",
        "",
        "A control does not need an external mapping to be valid. Organizations may adopt",
        "controls for internal policy, risk appetite, architecture, contractual, operational,",
        "or good-practice reasons. This catalog includes only mappings assessed as high",
        "confidence. It is not a complete crosswalk and does not establish compliance,",
        "conformity, certification, or legal applicability.",
        "",
        "- **Requirement:** the cited provision explicitly requires or directly addresses the control outcome.",
        "- **Guideline:** the cited provision supports the control as an implementation or maturity practice.",
        "- **Source-supported:** an identified source crosswalk or assessment supports the relationship.",
        "- **Inferred:** the relationship was independently reasoned from authoritative framework text.",
        "",
        "Regulatory mappings apply only when the organization, system, jurisdiction, role, and",
        "classification are in scope. Consult authoritative sources and qualified advisers.",
        "",
        f"**Published mappings:** {len(mappings)}",
        "",
        "## Mapping catalog",
        "",
        "| Control | Framework | Provision | Category | Basis | Condition | Rationale |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in mappings:
        condition = item.get("condition", "None stated")
        values = [
            item["control_id"], item["framework"], f"{item['edition']}: {item['reference']}",
            item["category"], item["basis"], condition, item["rationale"],
        ]
        escaped = [str(value).replace("|", "\\|").replace("\n", " ") for value in values]
        lines.append("| " + " | ".join(escaped) + " |")
    lines.extend([
        "", "## Deliberate gaps", "",
        "Controls absent from this catalog are intentionally unmapped. Add a mapping only when",
        "the relationship can be cited, explained, conditioned where necessary, and defended",
        "with high confidence. Do not add `unresolved` placeholders or force every control into",
        "each framework.", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    with SOURCE.open(encoding="utf-8") as stream:
        expected = render(yaml.safe_load(stream))
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print(f"{OUTPUT.relative_to(ROOT)} is not synchronized with {SOURCE.relative_to(ROOT)}")
            return 1
        return 0
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
