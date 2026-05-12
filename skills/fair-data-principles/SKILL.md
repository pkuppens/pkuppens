---
name: fair-data-principles
description: >-
  Guides application of FAIR data principles (Findable, Accessible,
  Interoperable, Reusable) when designing APIs, data models, and integration
  patterns. Use when designing APIs, data models, metadata schemas, or
  integration patterns where findability, accessibility, interoperability,
  or reusability are quality goals.
---

# FAIR Data Principles

Applies FAIR (Findable, Accessible, Interoperable, Reusable) as a crosscutting architectural concern to API design, data models, metadata, security, and data lineage. Originates from scientific data management ([Wilkinson et al., 2016](https://doi.org/10.1038/sdata.2016.18)) but applies broadly to healthcare, government, and enterprise data platforms.

**FAIR != Open Data.** Data can be private and still FAIR. Access control, authentication, and audit logging are part of "Accessible" — not barriers to it.

## When to use

- Designing REST or GraphQL APIs that expose datasets or domain resources
- Modelling data entities, metadata schemas, or catalogue records
- Integrating systems across organisations or domains (HL7 FHIR, SNOMED CT, ICD-10)
- Evaluating data platform quality attributes (findability, reusability, lineage)
- Reviewing API or data model PRs where FAIR compliance is a quality goal

## Principles overview

### F — Findable

Resources and their metadata must be easy to discover by humans and machines.

- Assign globally unique, persistent identifiers (UUID, URI, DOI)
- Attach rich, searchable metadata to every resource
- Register resources in a searchable catalogue or index
- Use consistent, descriptive naming conventions for endpoints and fields

### A — Accessible

Resources must be retrievable via standard protocols with clear authentication and authorisation rules.

- Serve over standard protocols (HTTPS, gRPC) with well-defined endpoints
- Implement authentication (OAuth2, JWT) and role-based authorisation
- Return machine-readable error responses with standard HTTP status codes
- Log access for audit; provide usage metadata (rate limits, quotas)
- Ensure metadata remains accessible even when the data itself is restricted

### I — Interoperable

Resources must use shared vocabularies and standard formats so different systems can exchange and interpret data.

- Use standard serialisation (JSON, XML, FHIR bundles)
- Reference established domain vocabularies (HL7 FHIR, SNOMED CT, ICD-10, LOINC)
- Publish API contracts via OpenAPI / AsyncAPI specifications
- Support content negotiation (`Accept` headers) for multiple formats
- Map internal models to standard external schemas at integration boundaries

### R — Reusable

Resources must be well-documented, versioned, and licensed so they can be used beyond the original context.

- Version APIs and data schemas (URL path, header, or media type versioning)
- Document provenance and data lineage (source, transformations, quality)
- Include licensing and usage terms in metadata responses
- Provide deprecation policies and migration guides for breaking changes
- Design schemas for extension (additional properties, profiles)

## Design checklist

Use this checklist when reviewing an API or data model design:

### Findable

- [ ] Every resource has a globally unique identifier (UUID, URI)
- [ ] Metadata is searchable (catalogue endpoint, OpenAPI tags)
- [ ] Naming follows a consistent convention (plural nouns, lowercase kebab)
- [ ] List endpoints support filtering, sorting, and pagination

### Accessible

- [ ] All endpoints use HTTPS with TLS 1.2+
- [ ] Authentication and authorisation are enforced (OAuth2 / JWT)
- [ ] Error responses follow a standard schema (RFC 9457 Problem Details)
- [ ] Access events are logged for audit

### Interoperable

- [ ] Request/response bodies use standard formats (JSON, XML)
- [ ] Domain terms reference established vocabularies where applicable
- [ ] An OpenAPI or AsyncAPI spec is published and kept in sync
- [ ] Content negotiation is supported for multi-format endpoints

### Reusable

- [ ] API version is explicit (URL path or header)
- [ ] Data lineage fields are present (source, created, modified, version)
- [ ] Deprecation policy is documented; sunset headers used for retiring endpoints
- [ ] Licence or usage terms are available in metadata responses

## Integration with other skills

- [architecture-crosscutting](../architecture/architecture-crosscutting/SKILL.md) — FAIR as a crosscutting quality attribute
- [api-design](../api-design/SKILL.md) — REST conventions that support FAIR
- [design-interfaces](../design/design-interfaces/SKILL.md) — API contract design
- [design-data-model](../design/design-data-model/SKILL.md) — entity and metadata modelling
- [requirements-goals](../requirements/requirements-goals/SKILL.md) — FAIR as a quality goal

## Additional resources

- [examples.md](examples.md) — C#/.NET and Python/FastAPI implementation patterns
