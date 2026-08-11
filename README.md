# AI Governance Control Framework

An independently authored, company-agnostic framework and machine-readable control library for governing enterprise AI capabilities and individual AI systems.

This repository is the authoritative source for the framework and control library. Applications, including the [AI Governance Control Plane](https://github.com/danvanbeeksec/ai-governance-control-plane), may consume a versioned release but do not define or duplicate the controls.

## What is included

- [Control Framework](docs/control-framework.md): architecture, applicability, evidence, and lifecycle
- [Control Domains](docs/control-domains.md): scope and boundaries of the seven domains
- [Implementation Guide](docs/implementation-guide.md): adoption and tailoring approach
- [Evidence Guide](docs/evidence-guide.md): evidence design and evaluation
- [Control Catalog](docs/control-catalog.md): generated human-readable view of all controls
- [Public References](docs/references.md): source citations and use limitations
- [`data/controls.yaml`](data/controls.yaml): authoritative 35-control library
- [Reference mappings](mappings/control-reference-mapping.md): conceptual public-source alignment
- [Synthetic assessment example](examples/sample-control-assessment.yaml): non-production usage example

## Installable distribution

The repository can be installed as a small Python package so consuming applications can use an
exact repository commit without copying the authoritative control library:

```bash
python -m pip install "ai-governance-control-framework @ git+https://github.com/danvanbeeksec/ai-governance-control-framework.git@<full-commit>"
```

Consumers can read the packaged artifact without modifying it:

```python
from ai_governance_control_framework import controls_bytes

artifact = controls_bytes()
```

The build includes the bytes from `data/controls.yaml`. Tests verify that the packaged resource
is identical to the authoritative artifact. The Python package is a distribution mechanism, not
a second control authority or an API for changing controls.

## Repository boundaries

The framework does not contain risk-tier logic, a control-selection engine, organization-specific approval authorities, legal conclusions, or employer-derived material. Mappings indicate conceptual relevance only. They do not establish compliance, conformity, certification, equivalence, or complete coverage.

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
```

## Status

**Initial framework milestone: ready for review.** The framework and 35-control baseline are complete enough for design review. Organization-specific tailoring, formal approval, and operational implementation remain outside this repository.

Licensed under the MIT License. See [LICENSE](LICENSE).
