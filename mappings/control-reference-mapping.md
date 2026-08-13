<!-- Generated from data/mappings.yaml. Do not edit directly. -->
# High-Confidence Framework Mappings

## Interpretation

A control does not need an external mapping to be valid. Organizations may adopt
controls for internal policy, risk appetite, architecture, contractual, operational,
or good-practice reasons. This catalog includes only mappings assessed as high
confidence. It is not a complete crosswalk and does not establish compliance,
conformity, certification, or legal applicability.

- **Requirement:** the cited provision explicitly requires or directly addresses the control outcome.
- **Guideline:** the cited provision supports the control as an implementation or maturity practice.
- **Source-supported:** an identified source crosswalk or assessment supports the relationship.
- **Inferred:** the relationship was independently reasoned from authoritative framework text.

Regulatory mappings apply only when the organization, system, jurisdiction, role, and
classification are in scope. Consult authoritative sources and qualified advisers.

**Published mappings:** 42

## Mapping catalog

| Control | Framework | Provision | Category | Basis | Condition | Rationale |
|---|---|---|---|---|---|---|
| AI-GOV-001 | ISO-IEC-42001 | 2023: 5.3; A.3.2 | requirement | source_supported | None stated | Directly addresses assigned AI roles, responsibilities, and authority. |
| AI-GOV-002 | ISO-IEC-42001 | 2023: 5.2; A.2.2; A.2.3 | requirement | source_supported | None stated | Directly addresses AI policy establishment, communication, and review. |
| AI-GOV-005 | ISO-IEC-42001 | 2023: 7.2; A.4.6 | requirement | source_supported | None stated | Directly addresses competence and human resources used across the AI lifecycle. |
| AI-GOV-006 | ISO-IEC-42001 | 2023: 9.2; 10.1; 10.2 | requirement | source_supported | None stated | Directly addresses internal audit, continual improvement, and corrective action. |
| AI-GOV-007 | ISO-IEC-42001 | 2023: 6.2; A.6.1.2; A.9.3 | requirement | source_supported | None stated | Directly addresses AI objectives and responsible development and use objectives. |
| AI-GOV-009 | ISO-IEC-42001 | 2023: 9.3 | requirement | source_supported | None stated | Directly addresses management review of the AI management system. |
| AI-GOV-010 | ISO-IEC-42001 | 2023: A.3.3; A.8.3 | requirement | source_supported | None stated | Directly addresses reporting AI concerns and adverse impacts. |
| AI-USE-002 | EU-AI-ACT | 2024: Article 4 | requirement | inferred | Applies to providers and deployers within the Act's scope. | Article 4 directly requires measures supporting a sufficient level of AI literacy. |
| AI-GOV-003 | ISO-IEC-27001 | 2022: A.5.9 | guideline | source_supported | None stated | The information and associated asset inventory control supports maintenance of an AI inventory. |
| AI-INV-002 | ISO-IEC-42001 | 2023: A.4.2-A.4.6 | requirement | source_supported | None stated | Directly addresses documentation of data, tooling, system, computing, and human resources. |
| AI-RSK-002 | ISO-IEC-42001 | 2023: A.5.2-A.5.5 | requirement | source_supported | None stated | Directly addresses an impact-assessment process and impacts on individuals, groups, and society. |
| AI-RSK-003 | ISO-IEC-42001 | 2023: 6.1; 8.1 | requirement | source_supported | None stated | Directly addresses risk treatment planning and operational implementation. |
| AI-GOV-004 | EU-AI-ACT | 2024: Article 9 | requirement | inferred | Applies to providers of high-risk AI systems. | Article 9 directly requires a documented, iterative risk-management system. |
| AI-DAT-003 | ISO-IEC-42001 | 2023: A.7.3-A.7.5 | requirement | source_supported | None stated | Directly addresses data acquisition, quality, and provenance. |
| AI-DAT-006 | ISO-IEC-42001 | 2023: A.7.6 | requirement | source_supported | None stated | Directly addresses criteria for AI data preparation. |
| AI-DAT-007 | ISO-IEC-42001 | 2023: A.7.4 | requirement | source_supported | None stated | Directly addresses defining and documenting AI data-quality requirements. |
| AI-DAT-007 | EU-AI-ACT | 2024: Article 10 | requirement | inferred | Applies to providers of high-risk AI systems using data-driven model development. | Article 10 directly addresses training, validation, and testing data governance and quality. |
| AI-LCM-001 | ISO-IEC-42001 | 2023: A.6.2.2; A.8.2 | requirement | source_supported | None stated | Directly addresses system requirements and information necessary for users. |
| AI-LCM-002 | ISO-IEC-42001 | 2023: A.6.2.4; A.6.2.5 | requirement | source_supported | None stated | Directly addresses verification, validation, and deployment readiness. |
| AI-MOD-003 | ISO-IEC-27001 | 2022: A.8.32 | guideline | source_supported | None stated | Formal change management directly supports controlled model and AI configuration changes. |
| AI-MOD-004 | ISO-IEC-42001 | 2023: A.6.2.4 | requirement | source_supported | None stated | Directly addresses defining and documenting AI verification and validation measures and criteria. |
| AI-SEC-002 | ISO-IEC-27001 | 2022: A.5.15-A.5.18; A.8.2-A.8.5 | guideline | source_supported | None stated | Access-control, identity, authentication, and privileged-access requirements support AI identity enforcement. |
| AI-SEC-002 | SOC-2 | 2017 with 2022 points of focus: CC6.1-CC6.3 | guideline | source_supported | None stated | Logical-access criteria support authentication, authorization, and least privilege for AI systems. |
| AI-PLT-002 | SOC-2 | 2017 with 2022 points of focus: CC6.2; CC6.3 | guideline | source_supported | None stated | Logical and privileged access criteria support controlled AI platform administration. |
| AI-SEC-005 | ISO-IEC-27001 | 2022: A.8.25-A.8.29 | guideline | source_supported | None stated | Secure development lifecycle and security-testing controls directly support secure AI application development. |
| AI-SEC-005 | SOC-2 | 2017 with 2022 points of focus: CC8.1 | guideline | source_supported | None stated | Change-management criteria support authorized, tested, and controlled AI development changes. |
| AI-HUM-001 | EU-AI-ACT | 2024: Article 14 | requirement | inferred | Applies to providers of high-risk AI systems and supports deployer oversight duties. | Article 14 directly requires effective human oversight measures for high-risk AI systems. |
| AI-HUM-003 | ISO-IEC-42001 | 2023: A.6.2.7; A.8.2; A.8.5 | requirement | source_supported | None stated | Directly addresses technical documentation and information for users and interested parties. |
| AI-HUM-003 | EU-AI-ACT | 2024: Article 13; Article 50 | requirement | inferred | Applies only to the relevant high-risk or transparency-triggering system and organizational role. | These provisions directly address instructions, transparency, and disclosure for specified AI systems. |
| AI-OPS-001 | ISO-IEC-42001 | 2023: A.6.2.8 | requirement | source_supported | None stated | Directly addresses enabling AI event logging at least while the system is in use. |
| AI-OPS-001 | EU-AI-ACT | 2024: Article 12 | requirement | inferred | Applies to providers of high-risk AI systems. | Article 12 directly requires automatic event logging over the system lifetime appropriate to its purpose. |
| AI-OPS-001 | ISO-IEC-27001 | 2022: A.8.15; A.8.16 | guideline | source_supported | None stated | Logging and monitoring controls support AI traceability and detection. |
| AI-OPS-001 | SOC-2 | 2017 with 2022 points of focus: CC7.2 | guideline | source_supported | None stated | Monitoring criteria support detection of anomalous AI events and activities. |
| AI-OPS-003 | ISO-IEC-27001 | 2022: A.5.24-A.5.28 | guideline | source_supported | None stated | Incident planning, assessment, response, learning, and evidence controls support AI incident handling. |
| AI-OPS-003 | DORA | 2022/2554: Articles 17-23 | guideline | inferred | Applies to an in-scope financial entity when the AI event is an ICT-related incident. | DORA directly addresses ICT incident management, classification, and reporting rather than AI incidents as a separate class. |
| AI-OPS-004 | DORA | 2022/2554: Articles 11-12 | guideline | inferred | Applies to in-scope financial entities and relevant ICT-supported functions. | DORA response, recovery, backup, restoration, and recovery procedures support resilient AI operations. |
| AI-OPS-004 | SOC-2 | 2017 with 2022 points of focus: A1.2; A1.3 | guideline | source_supported | None stated | Availability criteria support recovery, environmental protections, and tested continuity. |
| AI-VSC-001 | ISO-IEC-27001 | 2022: A.5.19; A.5.21 | guideline | source_supported | None stated | Supplier relationship and ICT supply-chain controls support AI supplier due diligence. |
| AI-VSC-001 | SOC-2 | 2017 with 2022 points of focus: CC9.2 | guideline | source_supported | None stated | Vendor and business-partner risk criteria support material AI supplier evaluation. |
| AI-VSC-002 | ISO-IEC-27001 | 2022: A.5.20 | guideline | source_supported | None stated | Supplier agreement controls support enforceable AI security and information-protection terms. |
| AI-VSC-004 | ISO-IEC-27001 | 2022: A.5.22 | guideline | source_supported | None stated | Supplier monitoring and change management directly support AI provider and subprocessor oversight. |
| AI-VSC-005 | DORA | 2022/2554: Articles 28-30 | guideline | inferred | Applies to in-scope contractual arrangements for ICT services. | DORA third-party risk provisions support concentration, continuity, contractual, and exit planning for AI ICT services. |

## Deliberate gaps

Controls absent from this catalog are intentionally unmapped. Add a mapping only when
the relationship can be cited, explained, conditioned where necessary, and defended
with high confidence. Do not add `unresolved` placeholders or force every control into
each framework.
