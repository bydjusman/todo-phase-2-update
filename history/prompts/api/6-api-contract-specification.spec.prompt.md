---
id: 6
title: api-contract-specification
stage: spec
date: 2026-02-16
surface: agent
model: if/qwen3-coder-plus
feature: api
branch: master
user: User
command: /sp.tasks
labels: [api, contract, rest, specification]
links:
  spec: /specs/api/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/api/tasks.md
tests:
---

## Prompt

```
SKILL: Design Clean REST API Contract

Create a clear, modern REST API specification.

Rules you must follow:
- Use resource-based URLs (plural nouns)
- Prefer /api/tasks over /api/{userId}/tasks when using JWT
- Use proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Return appropriate status codes (200, 201, 204, 400, 401, 403, 404, 422)
- Always require authentication via JWT → Authorization: Bearer <token>
- Response envelope: { data, meta?, error? }
- Use query params for filtering, sorting, pagination
- Use path params only for resource identifiers
- Return full resource on POST/PUT (or at least Location header + 201)
- Use PATCH for partial updates
- Support filtering by status, sorting by created_at/title, etc.

Output format:

# API: [Resource Name]

## Base Path
/api/[resource]

## Authentication
All endpoints require JWT in Authorization header

## Endpoints

### GET /api/tasks
Description: ...
Query params:
- status: "all" | "pending" | "completed"
- sort: "created_at" | "-created_at" | "title"
- page: integer
- limit: integer

Response 200:
```json
{
  "data": [ {task object}, ... ],
  "meta": { "total": 42, "page": 1, "limit": 20 }
}
```

```

## Response snapshot

Created comprehensive REST API contract specification for the tasks resource at /specs/api/tasks.md with:

- Resource-based URLs using plural nouns
- JWT authentication requirement with Authorization: Bearer header
- Proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Appropriate status codes (200, 201, 204, 400, 401, 403, 404, 422)
- Response envelope pattern with data, meta, and error fields
- Query parameters for filtering, sorting, and pagination
- Path parameters only for resource identifiers
- Full resource returns on POST/PUT operations
- PATCH for partial updates
- Filtering by status, sorting by created_at/title, with pagination
- Complete endpoint documentation with request/response schemas
- Error response examples for common scenarios

## Outcome

- ✅ Impact: Created complete REST API specification with modern best practices
- 🧪 Tests: No tests created as this was a specification task
- 📁 Files: Created specs/api/tasks.md
- 🔁 Next prompts: Implementation of API endpoints based on this specification
- 🧠 Reflection: Successfully created comprehensive API contract following all specified rules

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Extend API specification with additional resources