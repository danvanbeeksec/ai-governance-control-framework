# Changelog

## 1.1.0

- Added additive, machine-readable applicability metadata to every control.
- Defined supported AI contexts, applicability modes, factual trigger groups, required inputs, exclusions, and rationale.
- Preserved the original human-readable `applicability` field for existing consumers.
- Aligned the exported package version with the 1.1.0 distribution metadata.

All notable changes to the AI Governance Control Framework are recorded here.

## 1.0.0 - 2026-08-13

### Added

- A published baseline of 70 independently authored enterprise AI controls across 12 domains.
- Specific controls for general AI use, AI governance, inventory, lifecycle, risk and impact, data and privacy, AI systems, models, platforms, agents, human oversight, operations, vendors, and supply chains.
- A separate optional mapping library containing 42 high-confidence mappings to ISO/IEC 27001, ISO/IEC 42001, the EU AI Act, DORA, and SOC 2 Trust Services Criteria.
- Mapping metadata distinguishing Requirement from Guideline and source-supported from inferred relationships.
- A structured applicability taxonomy for future control-selection and automation use.
- Generated human-readable control and mapping catalogs.
- Package validation for the authoritative controls, mappings, and applicability artifacts.

### Compatibility

- The 35 control IDs published in the initial baseline remain unchanged.
- Risk-tier selection and control-recommendation logic remain outside this repository.
- Controls may remain intentionally unmapped when no high-confidence external relationship exists.

### Limitations

- Mappings do not establish legal applicability, compliance, conformity, certification, or assurance.
- Regulatory mappings depend on jurisdiction, organizational role, system classification, and sector scope.
- Adopters remain responsible for tailoring, approval, implementation, testing, and qualified legal or standards review.
