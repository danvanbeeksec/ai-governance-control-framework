# Evidence Guide

## Purpose

Evidence supports a conclusion about control design, implementation, or operation. It does not replace professional judgment, and evidence volume does not guarantee evidence quality.

## Evidence dimensions

| Dimension | Review question |
|---|---|
| Relevance | Does the evidence address the requirement, control object, and period under review? |
| Reliability | Is the source credible, reproducible, protected from inappropriate change, and sufficiently independent? |
| Coverage | Does it represent the relevant systems, versions, environments, populations, events, and time period? |
| Freshness | Is it still valid after changes in data, models, prompts, tools, permissions, vendors, or operating context? |

## Assurance states

- **Design:** the documented control is capable of achieving its objective if implemented as described.
- **Implementation:** the control exists in the system or process in scope.
- **Operating effectiveness:** the control operated consistently for the period and exceptions were handled appropriately.

These states should be recorded separately. A design document does not prove implementation, and a single successful test does not prove sustained operation.

## Evidence examples

Useful evidence may include approved records, inventories, architecture and data-flow diagrams, configuration exports, access reviews, contracts, evaluation plans and results, representative datasets, logs, alerts, incident exercises, tickets, exception approvals, change histories, and retirement records.

Self-attestation and screenshots can provide context, but they are normally stronger when corroborated by system-generated records, independent review, sampling, or repeatable tests.

## Evidence specification

For each implemented control, define the evidence owner, source system, collection method, expected fields, protected location, population or sample, period, frequency, retention, reviewer, acceptance criteria, exception handling, and conditions requiring refresh.

## Sensitive evidence

Prompts, outputs, traces, retrieval content, embeddings, model interactions, incident records, and security tests may contain personal, confidential, proprietary, or security-sensitive information. Apply minimization, access restrictions, secure transfer and storage, retention limits, and approved redaction. Do not place non-public employer or client evidence in this repository.
