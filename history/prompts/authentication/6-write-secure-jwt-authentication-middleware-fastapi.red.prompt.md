---
id: 6
title: Write Secure JWT Authentication Middleware for FastAPI
stage: red
date: 2026-02-16
surface: agent
model: Grok
feature: authentication
branch: main
user: user
command: 
labels: ["authentication", "jwt", "middleware", "fastapi", "security"]
links:
  spec: 
  ticket: 
  adr: 
  pr: 
files:
 - apps/server/middleware/auth.py
tests:
---

## Prompt

#### Skill 3: Write Secure JWT Authentication Middleware (Backend)
**For**: Backend Engineer Agent

```text
SKILL: Write Secure JWT Authentication Middleware (FastAPI)

You write secure, reusable JWT authentication logic for FastAPI.

Must follow these rules:

1. Read secret from environment variable: BETTER_AUTH_SECRET
2. Use python-jose or PyJWT (choose one consistently)
3. Verify signature, expiration, audience (if set)
4. Extract sub / user_id / email
5. Create dependency: get_current_user → returns user dict or raises 401/403
6. Add user to request.state.user
7. Protect routes with Depends(get_current_user)
8. Always filter database queries by current user id
9. Return 401 on missing/invalid token
10. Return 403 when user tries to access another user's resource

Output:
- auth.py file content (or relevant parts)
- Example usage in route
- Error handling patterns

Now implement secure JWT auth dependency for FastAPI.
```

## Response snapshot

Implemented secure JWT authentication middleware in /apps/server/middleware/auth.py with get_current_user dependency, ownership verification, and comprehensive route examples.

## Outcome

- ✅ Impact: Created secure JWT validation with user extraction and resource protection
- 🧪 Tests: No tests added yet
- 📁 Files: Created apps/server/middleware/auth.py
- 🔁 Next prompts: Implement Task API routes using this middleware
- 🧠 Reflection: Successfully implemented all security requirements with proper error handling and examples

## Evaluation notes (flywheel)

- Failure modes observed: 
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): 
- Next experiment (smallest change to try): </content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\history\prompts\authentication\6-write-secure-jwt-authentication-middleware-fastapi.red.prompt.md