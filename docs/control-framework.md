# Independent AI Control Framework

## Purpose

This framework provides a reusable structure for defining, applying, evidencing, and maintaining controls for organizational AI governance and individual AI systems. It is designed to stand on its own as a professional control-design asset. A governance platform may consume the library later, but the framework does not depend on a particular workflow, risk-tier model, product, vendor, or technology.

The framework translates broad governance and risk outcomes into testable requirements while preserving professional judgment. It is not a certification scheme, legal interpretation, complete regulatory crosswalk, or substitute for organization-specific risk assessment.

## Design principles

1. **Two control layers.** Enterprise governance capability and system-specific safeguards are related but distinct control objects.
2. **Outcome-oriented requirements.** Controls state the outcome that must be achieved without prescribing one product or implementation.
3. **Risk-responsive application.** Applicability follows system characteristics, context, and obligations. The library does not assign risk tiers.
4. **Evidence over assertion.** Implementation claims require evidence of design and, where relevant, operation.
5. **Lifecycle coverage.** Controls apply from concept and procurement through operation, change, and retirement.
6. **Technology neutrality.** Requirements cover internally developed, embedded, hosted, generative, predictive, and agentic AI.
7. **Independent authorship.** Control language is original, company-agnostic, and informed by public guidance without reproducing standards text.

## Scope and boundaries

The framework covers administrative and governance controls, technical security, data and privacy, lifecycle management, agentic AI, monitoring and operations, and vendor and supply-chain risk. It can support internal control design, architecture reviews, procurement, assessment, assurance planning, and future automation.

It does not contain:

- a risk-tier selection or recommendation engine;
- organization-specific approval authorities, thresholds, or workflows;
- jurisdiction-specific legal conclusions;
- a complete control test plan or evidence-retention schedule;
- claims of conformity with NIST, ISO/IEC, or OWASP material.

## Control architecture

### Layer 1: enterprise AI governance system controls

These controls ask whether the organization can govern AI consistently across a portfolio. Their control object is the management system: mandate, policy, accountability, inventory, risk process, competence, oversight, assurance, exceptions, and continual improvement.

Typical accountable parties include a governing body, executive sponsor, AI governance lead, and second- or third-line assurance functions. Evidence usually exists at organizational or portfolio level.

### Layer 2: individual AI system controls

These controls ask whether a specific use case is designed and operated within approved boundaries. Their control object includes data, models, prompts, retrieval sources, identities, permissions, tools, integrations, outputs, users, vendors, and runtime behavior.

Typical accountable parties include a business owner, product or system owner, engineering, security, privacy, data, model-risk, procurement, and operations teams. Evidence is normally tied to a named system and version.

### Shared and inherited controls

Some controls are implemented centrally and inherited by many AI systems, such as enterprise identity services, approved-vendor processes, logging infrastructure, or incident management. Inheritance must be explicit: record the provider, scope, dependencies, exclusions, and evidence. A central capability does not prove that each system is configured to use it correctly.

## Control domains

| Domain | Primary control outcomes | Typical layer |
|---|---|---|
| Administrative and governance | Mandate, accountability, policy, inventory, risk decisions, competence, assurance | Enterprise, with system ownership requirements |
| Technical and security | Secure architecture, access, input and output handling, component security, resilience | AI system |
| Data and privacy | Authorized data use, minimization, provenance, protection, retention, individual rights | Both |
| Lifecycle | Intake, documented purpose, testing, release, change, reassessment, retirement | Both |
| Agentic AI | Agent identity, delegated authority, tool boundaries, memory, approvals, containment | AI system |
| Monitoring and operations | Logging, behavioral monitoring, performance, incident response, recovery | Both |
| Vendor and supply chain | Due diligence, contract safeguards, component provenance, changes, dependency and exit | Both |

## Control record model

Each entry in `data/controls.yaml` contains:

| Field | Meaning |
|---|---|
| `control_id` | Stable identifier. IDs describe domain, not priority or standard ownership. |
| `domain` | One of the seven framework domains. |
| `layer` | `enterprise`, `ai_system`, or `both`. |
| `title` | Short, recognizable control name. |
| `objective` | Risk or governance outcome the control is intended to achieve. |
| `requirement` | Normative, independently authored statement of what must be done. |
| `applicability` | Conditions that make the control relevant. It is not a risk-tier rule. |
| `evidence_examples` | Illustrative evidence, not an exhaustive test procedure. |
| `implementation_notes` | Technology-neutral design considerations and common boundaries. |
| `references` | Public-source identifiers showing conceptual relevance. |

The library separates a control objective from its implementation. An organization may create procedures, technical standards, tests, and evidence specifications beneath a control without changing the stable control ID.

## Applicability model

Every control should be evaluated using system facts and organizational obligations. Relevant triggers include:

- enterprise-wide governance responsibility;
- production or externally available use;
- personal, confidential, regulated, or safety-relevant data;
- consequential decisions or material external communications;
- retrieval-augmented generation or untrusted content ingestion;
- tool, connector, code-execution, credential, or write access;
- persistent memory, multi-agent delegation, or autonomous action;
- third-party models, hosting, data, libraries, plugins, or services;
- material changes to purpose, model, data, permissions, reach, or operating context.

Applicability decisions should use these states:

- `applicable`: an owner and evidence are required;
- `not_applicable`: rationale and appropriate approval are recorded;
- `planned`: applicable but not yet implemented;
- `implemented`: the design exists, but operating effectiveness is not established;
- `verified`: evidence supports the required design and operation;
- `exception`: an authorized, time-bound deviation records conditions and residual risk.

## Evidence model

Evidence should be assessed across four dimensions:

1. **Relevance:** it addresses the stated requirement and the system in scope.
2. **Reliability:** its source, integrity, and method are credible.
3. **Coverage:** it represents the relevant versions, environments, populations, and time period.
4. **Freshness:** it remains valid after changes in the system or threat environment.

Evidence may demonstrate design, implementation, or operating effectiveness. Examples include approved records, architecture and data-flow diagrams, configuration exports, access reviews, contracts, inventories, test results, evaluation datasets, logs, alerts, incident exercises, tickets, and retirement records. A screenshot or self-attestation alone may be useful context but rarely proves sustained operation.

Evidence collection must itself respect privacy, confidentiality, security, minimization, and retention requirements. Prompts, outputs, traces, and model interactions can contain sensitive information.

## Control lifecycle

1. **Propose:** identify a risk outcome, control objective, affected layer, and public-source rationale.
2. **Design:** write a technology-neutral requirement and define applicability, evidence, and ownership expectations.
3. **Review:** challenge necessity, clarity, testability, duplication, feasibility, and unintended effects.
4. **Approve:** authorize the control through the organization’s governance process.
5. **Implement:** establish procedures, technical mechanisms, responsible owners, and evidence sources.
6. **Verify:** assess design and operation at a frequency proportionate to risk and change.
7. **Maintain:** version requirements and mappings when technology, incidents, obligations, or guidance change.
8. **Retire:** preserve decision history, supersession, and any continuing evidence obligations.

Material control changes should record the reason, approver, effective date, affected systems, migration expectations, and whether reassessment is required. Stable IDs should not be reused for a different objective.

## Governance and technical-control relationship

Governance controls create the conditions for sound system decisions; technical controls enforce boundaries within a system. Neither substitutes for the other.

For example, an enterprise policy may require least privilege and documented accountability. A particular agent then needs its own identity, scoped credentials, allowed tools, approval gates, and monitored actions. Conversely, a well-configured agent does not establish an organization-wide inventory, risk process, exception authority, or assurance program.

The relationship should be traceable:

```text
enterprise mandate and policy
  -> system ownership and assessment
  -> applicable system controls
  -> implementation and evidence
  -> monitoring, incidents, and reassessment
  -> portfolio oversight and continual improvement
```

## Using the framework as a standalone asset

The framework and YAML library may be used independently for workshops, control design, architecture review, vendor diligence, gap assessment, and educational demonstrations. A consumer should tailor applicability, ownership, evidence sufficiency, test procedures, and review frequency to its context. See the [Implementation Guide](implementation-guide.md) and [Evidence Guide](evidence-guide.md).

Any future governance control plane should import the library as versioned reference data. Risk-tier selection, recommendations, exceptions, evidence workflow, and runtime enforcement should remain separate services or modules so they can evolve without rewriting the control source.

## Public-source relationship and limitations

The controls are informed by NIST AI RMF 1.0, the NIST Generative AI Profile, ISO/IEC 42001, ISO/IEC 23894, the OWASP Top 10 for LLM Applications, and OWASP agentic AI guidance. See [Control Reference Mapping](../mappings/control-reference-mapping.md) and [Public References](references.md).

Mappings show thematic alignment only. They do not reproduce copyrighted standard text, establish clause-level coverage, demonstrate conformity, or replace review of the authoritative publications. The framework requires organization-specific legal, regulatory, privacy, security, safety, operational, and risk review before production use.
