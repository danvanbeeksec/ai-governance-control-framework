# AI Control Reference Mapping

## Purpose and interpretation

This document maps the independently authored controls in `data/controls.yaml` to public AI governance and security references. It helps reviewers understand why a control domain is relevant and where to perform deeper research.

Mappings are **conceptual and non-exhaustive**. They do not reproduce source requirements, represent a clause-by-clause crosswalk, demonstrate full coverage, establish equivalence, or support a claim of compliance, conformity, or certification. Readers should consult the authoritative publications and obtain qualified advice for their context. ISO/IEC standard text is not reproduced.

## Source keys

| Key | Public reference | Mapping use |
|---|---|---|
| NIST-AI-RMF | NIST AI RMF 1.0 | Governance, context, measurement, management, accountability, and lifecycle outcomes |
| NIST-AI-600-1 | NIST Generative AI Profile | Generative AI risks and suggested actions organized around AI RMF outcomes |
| ISO-IEC-42001 | ISO/IEC 42001:2023 | AI management-system, governance, operation, evaluation, and improvement context |
| ISO-IEC-23894 | ISO/IEC 23894:2023 | AI risk-management principles, integration, process, monitoring, and communication context |
| OWASP-LLM | OWASP Top 10 for LLM Applications 2025 | LLM application threat categories and security design context |
| OWASP-AGENTIC | OWASP Top 10 for Agentic Applications 2026 | Agent goals, tools, identity, code, memory, communications, cascades, trust, and rogue behavior |
| OWASP-AGENTIC-STATE | OWASP State of Agentic AI Security and Governance | Agent taxonomy, runtime identity, permissions, observability, governance, and containment context |

Full citations and links are maintained in [Public References](../docs/references.md).

## Domain-level mapping

| Control domain | NIST AI RMF | NIST AI 600-1 | ISO/IEC 42001 | ISO/IEC 23894 | OWASP LLM | OWASP agentic guidance |
|---|---|---|---|---|---|---|
| Administrative and governance | Primary | Primary | Primary | Primary | Supporting | Supporting |
| Technical and security | Primary | Primary | Supporting | Supporting | Primary | Primary |
| Data and privacy | Primary | Primary | Primary | Primary | Primary | Supporting |
| Lifecycle | Primary | Primary | Primary | Primary | Supporting | Supporting |
| Agentic AI | Supporting | Primary | Supporting | Supporting | Supporting | Primary |
| Monitoring and operations | Primary | Primary | Primary | Primary | Supporting | Primary |
| Vendor and supply chain | Primary | Primary | Primary | Primary | Primary | Primary |

`Primary` means the source is a central basis for the domain. `Supporting` means it offers relevant context but is not relied on as a complete treatment.

## Control-level mapping

| Control ID | Control title | Public-reference alignment |
|---|---|---|
| AI-GOV-001 | AI governance mandate and decision rights | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894 |
| AI-GOV-002 | AI policy and acceptable-use boundaries | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001 |
| AI-GOV-003 | AI inventory and accountable ownership | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894; OWASP-AGENTIC-STATE |
| AI-GOV-004 | AI risk and impact assessment | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; ISO-IEC-23894 |
| AI-GOV-005 | Competence and role-based awareness | NIST-AI-RMF; ISO-IEC-42001 |
| AI-GOV-006 | Independent challenge and continual improvement | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894 |
| AI-SEC-001 | Secure architecture and threat modeling | NIST-AI-RMF; NIST-AI-600-1; OWASP-LLM; OWASP-AGENTIC |
| AI-SEC-002 | Identity, authentication, and least privilege | OWASP-LLM; OWASP-AGENTIC; OWASP-AGENTIC-STATE; NIST-AI-RMF |
| AI-SEC-003 | Untrusted input and prompt-injection defenses | OWASP-LLM; OWASP-AGENTIC; NIST-AI-600-1 |
| AI-SEC-004 | Safe output handling | OWASP-LLM; OWASP-AGENTIC |
| AI-SEC-005 | Secure development, testing, and vulnerability management | OWASP-LLM; OWASP-AGENTIC; NIST-AI-RMF |
| AI-SEC-006 | Resource and service abuse protection | OWASP-LLM; OWASP-AGENTIC; NIST-AI-600-1 |
| AI-DAT-001 | Authorized data use and minimization | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; ISO-IEC-23894 |
| AI-DAT-002 | Data classification and protection | NIST-AI-RMF; NIST-AI-600-1; OWASP-LLM; ISO-IEC-42001 |
| AI-DAT-003 | Data provenance, quality, and permitted sourcing | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; OWASP-LLM |
| AI-DAT-004 | Privacy assessment and individual protections | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; ISO-IEC-23894 |
| AI-LCM-001 | Intended use, limitations, and success criteria | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; ISO-IEC-23894 |
| AI-LCM-002 | Evaluation, validation, and release readiness | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; OWASP-LLM; OWASP-AGENTIC |
| AI-LCM-003 | Material change and reassessment | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894; OWASP-AGENTIC |
| AI-LCM-004 | Suspension and retirement | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894 |
| AI-AGT-001 | Agent identity and delegated authority | OWASP-AGENTIC; OWASP-AGENTIC-STATE; NIST-AI-600-1 |
| AI-AGT-002 | Tool, connector, and action boundaries | OWASP-AGENTIC; OWASP-AGENTIC-STATE; OWASP-LLM |
| AI-AGT-003 | Human approval and irreversible-action safeguards | OWASP-AGENTIC; OWASP-AGENTIC-STATE; NIST-AI-RMF |
| AI-AGT-004 | Agent memory and state protection | OWASP-AGENTIC; OWASP-AGENTIC-STATE; NIST-AI-600-1 |
| AI-AGT-005 | Multi-agent and delegation controls | OWASP-AGENTIC; OWASP-AGENTIC-STATE |
| AI-AGT-006 | Agent containment and emergency stop | OWASP-AGENTIC; OWASP-AGENTIC-STATE; NIST-AI-600-1 |
| AI-OPS-001 | Logging and traceability | NIST-AI-RMF; NIST-AI-600-1; OWASP-AGENTIC-STATE; OWASP-LLM |
| AI-OPS-002 | Behavioral and control monitoring | NIST-AI-RMF; NIST-AI-600-1; OWASP-AGENTIC-STATE; ISO-IEC-42001 |
| AI-OPS-003 | AI incident response and reporting | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; OWASP-AGENTIC-STATE |
| AI-OPS-004 | Resilience, safe failure, and recovery | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894; OWASP-AGENTIC |
| AI-VSC-001 | AI supplier and service due diligence | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; ISO-IEC-23894; OWASP-LLM |
| AI-VSC-002 | Contractual AI safeguards | NIST-AI-RMF; NIST-AI-600-1; ISO-IEC-42001; ISO-IEC-23894 |
| AI-VSC-003 | Component provenance and integrity | OWASP-LLM; OWASP-AGENTIC; NIST-AI-600-1 |
| AI-VSC-004 | Supplier change and subprocessor oversight | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894; OWASP-LLM |
| AI-VSC-005 | Concentration, continuity, and exit planning | NIST-AI-RMF; ISO-IEC-42001; ISO-IEC-23894 |

## Security-threat coverage view

The following view helps practitioners locate controls for common LLM and agentic threat themes. It is not an OWASP compliance matrix.

| Threat theme | Most relevant controls |
|---|---|
| Prompt or instruction manipulation | AI-SEC-001, AI-SEC-003, AI-SEC-004, AI-AGT-002, AI-LCM-002 |
| Sensitive information disclosure | AI-DAT-001, AI-DAT-002, AI-DAT-004, AI-SEC-002, AI-SEC-004, AI-OPS-001 |
| Supply-chain or component compromise | AI-VSC-001, AI-VSC-003, AI-VSC-004, AI-SEC-005, AI-LCM-003 |
| Data or model poisoning | AI-DAT-003, AI-SEC-001, AI-LCM-002, AI-AGT-004, AI-OPS-002 |
| Unsafe model output or code | AI-SEC-004, AI-AGT-002, AI-AGT-003, AI-LCM-002, AI-OPS-002 |
| Excessive agency or privilege abuse | AI-SEC-002, AI-AGT-001, AI-AGT-002, AI-AGT-003, AI-AGT-006 |
| Memory manipulation or leakage | AI-DAT-002, AI-DAT-004, AI-AGT-004, AI-OPS-001, AI-OPS-002 |
| Inter-agent trust and cascading failure | AI-AGT-005, AI-AGT-006, AI-OPS-001, AI-OPS-002, AI-OPS-004 |
| Resource exhaustion or runaway cost | AI-SEC-006, AI-AGT-002, AI-AGT-005, AI-AGT-006, AI-OPS-002 |
| Overreliance or ineffective oversight | AI-GOV-005, AI-LCM-001, AI-LCM-002, AI-AGT-003, AI-OPS-002 |

## Known gaps and future overlays

The initial library intentionally provides a cross-industry baseline. Before operational use, most organizations will need additional overlays or implementation standards for:

- jurisdiction-specific AI, privacy, employment, consumer, financial-services, health, safety, and records obligations;
- sector-specific model risk management and validation;
- fairness, accessibility, civil-rights, and consequential-decision testing methods;
- child safety, physical safety, cybersecurity product, or critical-infrastructure use;
- intellectual-property, content provenance, disclosure, and synthetic-media obligations;
- environmental and computational-resource measurement;
- detailed secure-configuration baselines for particular platforms and agent runtimes;
- quantitative evaluation thresholds, sampling, test independence, and evidence-retention periods;
- control test procedures and operating-effectiveness criteria;
- risk-tier and scenario selection logic, which is deliberately deferred.

These are not omissions to solve by silently expanding every baseline control. They should be explicit overlays with accountable subject-matter review.
