# AI Governance Control Framework

Version 1.2 normalizes the public Agent Baseline v1.0-draft concepts into the existing common-control architecture. It adds no parallel Agent Baseline controls and does not replace the current applicability model.

See [Applicability metadata](docs/applicability-metadata.md) for the machine-readable contract and compatibility guidance.

An independently authored, company-agnostic framework and machine-readable control library for governing enterprise AI capabilities and individual AI systems.

This repository is the authoritative source for the framework and control library. Applications, including the [AI Governance Control Plane](https://github.com/danvanbeeksec/ai-governance-control-plane), may consume a versioned release but do not define or duplicate the controls.

## What is included

- [Control Framework](docs/control-framework.md): architecture, applicability, evidence, and lifecycle
- [Control Domains](docs/control-domains.md): scope and boundaries of the enterprise control domains
- [Implementation Guide](docs/implementation-guide.md): adoption and tailoring approach
- [Evidence Guide](docs/evidence-guide.md): evidence design and evaluation
- [Control Catalog](docs/control-catalog.md): generated human-readable view of all controls
- [Public References](docs/references.md): source citations and use limitations
- [Changelog](CHANGELOG.md): version history and compatibility notes
- [`data/controls.yaml`](data/controls.yaml): authoritative 70-control library
- [`data/mappings.yaml`](data/mappings.yaml): optional, high-confidence requirement and guideline mappings
- [`data/agent-baseline-crosswalk.yaml`](data/agent-baseline-crosswalk.yaml): non-authoritative traceability from all 35 Agent Baseline v1.0-draft controls to existing canonical controls
- [Reference mappings](mappings/control-reference-mapping.md): human-readable mapping methodology and catalog
- [Synthetic assessment example](examples/sample-control-assessment.yaml): non-production usage example

## Installable distribution

The repository can be installed as a small Python package so consuming applications can use an
exact repository commit without copying the authoritative control library:

```bash
python -m pip install "ai-governance-control-framework @ git+https://github.com/danvanbeeksec/ai-governance-control-framework.git@<full-commit>"
```

Consumers can read the packaged artifact without modifying it:

```python
from ai_governance_control_framework import agent_baseline_crosswalk_bytes, controls_bytes, mappings_bytes

artifact = controls_bytes()
optional_mappings = mappings_bytes()
agent_baseline_traceability = agent_baseline_crosswalk_bytes()
```

The build includes the bytes from `data/controls.yaml`. Tests verify that the packaged resource
is identical to the authoritative artifact. The Python package is a distribution mechanism, not
a second control authority or an API for changing controls.

## Repository boundaries

The framework does not contain risk-tier logic, a control-selection engine, organization-specific approval authorities, legal conclusions, or employer-derived material. A control does not need an external mapping to be valid. Published mappings are limited to high-confidence relationships and do not establish compliance, conformity, certification, equivalence, or complete coverage.

No employer or client control catalog, policy, assessment, evidence, workflow, architecture, identifier, threshold, or non-public data may be added to this repository. Examples must use fictional organizations, systems, and outcomes.

## Validate the library

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

`docs/control-catalog.md` is generated from the authoritative YAML library. After
changing `data/controls.yaml`, regenerate it with:

```bash
python scripts/render_control_catalog.py
python scripts/render_mapping_catalog.py
```

## Status

**Version 1.2 is published.** The library retains 70 enterprise AI controls across 12 domains, adds non-authoritative Agent Baseline draft traceability without creating duplicate authority, and leaves organization-specific tiering, tailoring, approval, and implementation to each adopter. The source crosswalk remains explicitly draft and must be reassessed if Agent Baseline changes or leaves draft status.

Licensed under the MIT License. See [LICENSE](LICENSE).
