# Control Domains

The v1.0 release candidate contains 70 controls across twelve deliberately specific domains.
The additional domains keep general workforce use, inventory, impact, models and platforms,
and human oversight visible instead of forcing those requirements into generic system controls.

## Purpose

Domains support navigation and ownership discussions; they are not organizational silos. A single risk scenario may require controls from several domains.

| Domain key | Domain | Scope |
|---|---|---|
| `administrative_governance` | Administrative and governance | Mandate, policy, accountability, inventory, assessment, competence, assurance, and continual improvement |
| `technical_security` | Technical and security | Architecture, identity, input and output handling, secure development, vulnerability management, and resource protection |
| `data_privacy` | Data and privacy | Authorized use, minimization, classification, protection, provenance, quality, retention, and individual protections |
| `lifecycle` | Lifecycle | Intended use, acceptance criteria, evaluation, release, material change, reassessment, suspension, and retirement |
| `agentic_ai` | Agentic AI | Agent identity, delegated authority, tools, approvals, memory, multi-agent operation, containment, and emergency stop |
| `monitoring_operations` | Monitoring and operations | Traceability, behavioral monitoring, incident response, safe failure, resilience, and recovery |
| `vendor_supply_chain` | Vendor and supply chain | Supplier diligence, contracts, component provenance, changes, subprocessors, concentration, continuity, and exit |
| `usage_workforce` | AI usage and workforce | Approved tools, literacy, output verification, and information-use boundaries |
| `inventory_lifecycle` | Inventory and lifecycle governance | Discovery, dependency documentation, registration, ownership, and lifecycle status |
| `risk_impact_compliance` | Risk, impact, and compliance | Regulatory classification, impact assessment, treatment, and acceptance |
| `systems_models_platforms` | Systems, models, and platforms | Model approval, versioning, evaluation, platform isolation, administration, and endpoints |
| `human_oversight_transparency` | Human oversight and transparency | Oversight authority, decision accountability, contestability, disclosure, and user information |

## Enterprise and system layers

`enterprise` controls operate across an AI portfolio or management system. `ai_system` controls apply to a named system or use case. `both` indicates a shared outcome that requires enterprise capability and system-level execution.

Layer assignment does not determine ownership. Organizations should identify an accountable owner, implementers, reviewers, evidence providers, and approval authority for every applicable control.

## Domain boundaries

- Data protection requirements complement, but do not replace, secure architecture and access controls.
- Lifecycle evaluation complements, but does not replace, operational monitoring after release.
- Agentic controls extend baseline security and governance controls when a system can plan, delegate, use tools, retain state, or take action.
- Vendor controls address external dependency risk. They do not transfer accountability to a supplier.
- Governance controls establish decision rights and oversight. They do not prove that a system is technically safe.

## Overlays

The baseline is cross-industry. Legal, regulatory, sector, jurisdiction, technology, and risk-tier overlays should be maintained separately, with qualified review and an explicit relationship to stable control IDs. An overlay should not silently change the meaning of a baseline requirement.
