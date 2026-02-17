---
id: 4
title: backend-jwt-auth-implementation
stage: spec
date: 2026-02-16
surface: agent
model: if/qwen3-coder-plus
feature: backend
branch: master
user: User
command: /sp.tasks
labels: [backend, jwt, authentication, fastapi, tasks]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - apps/server/auth.py
 - apps/server/api/routes/tasks.py
 - apps/server/models/task.py
 - apps/server/database/session.py
 - apps/server/models/__init__.py
tests:
---

## Prompt

```
You are the Backend Engineer Agent.

Implement the FastAPI JWT authentication dependency and the GET /api/tasks endpoint.

Use:
- PyJWT or python-jose for verification
- Secret from env (BETTER_AUTH_SECRET)
- Dependency that returns current user id/email
- Filter tasks by authenticated user only

Provide code for:
- auth.py (get_current_user dep)
- routes/tasks.py (list tasks)
```

## Response snapshot

Implemented the FastAPI JWT authentication system and GET /api/tasks endpoint with the following components:

1. Created `apps/server/auth.py` with:
   - JWT token verification using python-jose
   - HTTP Bearer security scheme
   - get_current_user dependency that extracts and validates user info from JWT
   - TokenData model for user information
   - Proper error handling for invalid credentials

2. Created `apps/server/api/routes/tasks.py` with:
   - GET /api/tasks endpoint that lists tasks
   - Authentication dependency using get_current_user
   - Filtering of tasks by authenticated user
   - Proper imports and database session dependency

3. Created supporting files:
   - `apps/server/models/task.py` with proper Task model
   - `apps/server/database/session.py` with database session dependency
   - `apps/server/models/__init__.py` for proper module structure

All code properly implements JWT authentication using BETTER_AUTH_SECRET from environment variables and filters tasks by the authenticated user.

## Outcome

- ✅ Impact: Implemented JWT authentication system and authenticated tasks endpoint
- 🧪 Tests: No tests created as this was an implementation task
- 📁 Files: Created/modified auth.py, routes/tasks.py, models/task.py, database/session.py
- 🔁 Next prompts: Implementation of remaining task endpoints (create, update, delete)
- 🧠 Reflection: Successfully implemented secure authentication system with proper user isolation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add additional task endpoints (POST, PUT, DELETE)