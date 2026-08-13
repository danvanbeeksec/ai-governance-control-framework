# Applicability metadata

Each control retains its human-readable `applicability` statement and adds an `applicability_metadata` object. This is an additive contract intended for deterministic consumers.

- `contexts` identifies relevant AI object types, such as general AI usage, AI systems, platforms, agents, models, data, or vendor AI.
- `mode` is `universal`, `conditional`, or `human_determination`.
- `trigger_conditions` contains OR groups. Every condition within one group's `all` list must match.
- `required_inputs` names the assessment facts used by those conditions.
- `exclusions` records explicit exclusions when the framework supports them. An empty list means that no exclusion is asserted.
- `rationale` explains why the applicability declaration exists.

The framework does not evaluate these declarations. A decision service validates submitted facts, evaluates supported operators, preserves provenance, and returns an applicability outcome. A missing trigger does not imply that a control is not applicable unless an explicit exclusion supports that conclusion.

## Compatibility

Existing consumers can continue reading the unchanged `applicability` string. Strict consumers that reject additional fields must update their schema for framework schema 2.1. Consumers should fail closed on unsupported operators or unknown assessment fields.
