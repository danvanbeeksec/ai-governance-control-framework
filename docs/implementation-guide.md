# Implementation Guide

## Purpose

This guide describes how to adopt the framework without treating a generic library as a finished control environment.

## Adoption sequence

1. Define the governed population, including acquired, embedded, experimental, internally developed, generative, predictive, and agentic uses.
2. Establish accountable governance, system ownership, decision rights, and exception authority.
3. Evaluate each control for applicability using system facts, obligations, threats, and operating context.
4. Assign owners and identify whether implementation is central, system-specific, inherited, or shared.
5. Create procedures, technical standards, test steps, evidence requirements, and review frequencies beneath the stable control IDs.
6. Record gaps, approved exceptions, compensating measures, residual risk, due dates, and accountable decisions.
7. Verify design and operation before representing a control as effective.
8. Reassess after material change, incidents, new obligations, control failure, or changes to the framework.

## Tailoring rules

- Preserve the original `control_id`, objective, and requirement when claiming use of the baseline.
- Record additions as organization-specific overlays or implementation standards.
- Document `not_applicable` decisions with rationale and appropriate approval.
- Do not infer applicability solely from a risk tier. Consider data, reach, impact, autonomy, tools, identities, external dependencies, and legal or contractual obligations.
- Do not infer effectiveness from policy publication, configuration screenshots, or owner attestation alone.

## Inherited controls

For a centrally provided control, record the service provider, covered requirement, supported systems, configuration dependencies, exclusions, evidence source, review period, and failure escalation. The consuming system must still demonstrate that it is correctly configured and within the inheritance scope.

## Versioning and change

Consumers should pin an explicit library version or commit. A framework update should not change a production decision silently. Review release notes, identify affected control IDs, assess implementation and evidence impact, approve the adoption decision, and retain the prior decision history.

## Control Plane integration

The AI Governance Control Plane is a consumer, not an authority. Consuming applications may install an exact framework repository commit and read the packaged `data/controls.yaml` bytes. They must still validate schema and integrity, record the source version with each decision, and keep risk classification and recommendation logic separate from the control source. Packaging is a distribution mechanism and does not create a second control authority.

## Completion criteria

Adoption is complete only when scope, ownership, applicability, implementation, test methods, evidence, exceptions, review frequency, versioning, and change governance are defined and approved for the adopting organization.
