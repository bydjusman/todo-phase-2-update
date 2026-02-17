<!--
Sync Impact Report:
Version change: N/A → 1.0.0
Modified principles: None (new constitution)
Added sections: All sections
Removed sections: None
Templates requiring updates: ⚠ pending (plan-template.md, spec-template.md, tasks-template.md, commands)
Follow-up TODOs: None
-->
# Todo Web App Constitution

## Core Principles

### I. API-First Design
All features must begin with a well-defined API contract documented in specs/api/. Endpoints follow RESTful principles with consistent response formats, proper HTTP status codes, and comprehensive error handling. Before implementing any feature, the API contract must be reviewed and approved.

### II. Security-First Architecture
Security is built into every layer, not added afterward. All endpoints require JWT authentication, sensitive data is never logged, passwords are properly hashed, and CSRF protection is implemented. Authentication uses industry-standard libraries like Better Auth with proper token management.

### III. Test-Driven Development (NON-NEGOTIABLE)
TDD is mandatory: Tests written first → User requirements approved → Tests fail initially → Then implement → Refactor. All code must have corresponding tests with reasonable coverage thresholds. Red-Green-Refactor cycle is strictly enforced for all implementations.

### IV. Type Safety & Validation
All code must be strongly typed using TypeScript on the frontend and appropriate type systems on the backend. Input validation occurs at API boundaries using schema validation libraries like Zod or Pydantic. Runtime validation ensures data integrity throughout the application.

### V. Performance & Observability
Performance is a feature: all API endpoints must respond within 500ms for 95% of requests. Comprehensive logging and metrics collection enables monitoring and debugging. Critical paths are instrumented to enable rapid issue identification and resolution.

### VI. Clean Architecture & Modularity
Code follows clean architecture principles with clear separation of concerns. Business logic is separated from infrastructure, components have single responsibilities, and dependencies flow inward. This ensures maintainability and testability of the codebase.

## Additional Security Requirements

### Authentication & Authorization
- All API endpoints require valid JWT tokens in Authorization header
- User data isolation through user_id foreign key validation
- Session management with proper timeout and refresh mechanisms
- Password requirements: minimum 8 characters, mixed case, numbers, special characters

### Data Protection
- Sensitive data encryption at rest and in transit
- No PII logged to standard logs
- Regular security scanning of dependencies
- Input sanitization to prevent injection attacks

## Development Workflow

### Code Review Process
- All code changes require peer review before merging
- PRs must reference feature specifications from specs/features/
- Code must pass all tests and linting checks
- Architecture decisions must align with documented plans

### Testing Standards
- Unit tests for all business logic components
- Integration tests for API endpoints
- End-to-end tests for critical user flows
- Performance tests for any database queries or complex operations

### Quality Gates
- 80% test coverage minimum for new features
- All automated tests must pass before merge
- Security scanning must pass
- Linting and formatting checks must pass

## Governance

This constitution supersedes all other development practices and standards. Amendments require explicit documentation, team approval, and a migration plan for existing code. All pull requests and code reviews must verify compliance with these principles. Complexity must be justified with clear benefits, and the guidance in CLAUDE.md provides runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2026-02-16 | **Last Amended**: 2026-02-16
