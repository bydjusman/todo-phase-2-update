---
id: 9
title: implementation-planning
stage: plan
date: 2026-02-16
surface: agent
model: if/qwen3-coder-plus
feature: full-stack-todo-app
branch: 1-full-stack-todo-app
user: User
command: /sp.plan
labels: [planning, architecture, api-design, data-model]
links:
  spec: /specs/1-full-stack-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-full-stack-todo-app/plan/plan.md
 - specs/1-full-stack-todo-app/research.md
 - specs/1-full-stack-todo-app/data-model.md
 - specs/1-full-stack-todo-app/contracts/tasks.yaml
 - specs/1-full-stack-todo-app/quickstart.md
tests:
---

## Prompt

```
# /specs/plan.md
# Phase 2 Development Plan – Hackathon Todo Full-Stack Web Application

Version: 1.0
Phase: II – Multi-user Web Application with Authentication & Persistent Storage
Goal: Build a secure, multi-user Todo app with Next.js frontend, FastAPI backend, Neon PostgreSQL, and Better Auth + JWT

## 1. High-Level Phases of Phase 2

| Order | Phase Name                        | Main Deliverables                                      | Estimated Effort | Dependencies                     |
|-------|-----------------------------------|--------------------------------------------------------|------------------|----------------------------------|
| 1     | Setup & Foundation                | Monorepo, env, docker-compose, basic project skeletons | Small            | —                                |
| 2     | Database & Models                 | Schema, connection, SQLModel models                    | Medium           | Phase 1                          |
| 3     | Authentication – Backend          | JWT verification middleware & dependency               | Medium           | Phase 2                          |
| 4     | Authentication – Frontend         | Better Auth setup, login/signup/logout pages           | Medium           | Phase 3                          |
| 5     | Core Task CRUD – Backend          | All task endpoints + ownership enforcement             | Large            | Phase 3                          |
| 6     | Core Task CRUD – Frontend         | Task list, create, edit, delete, toggle UI             | Large            | Phase 4 + 5                      |
| 7     | API Client & Auth Integration     | Secure API fetch wrapper with token handling           | Medium           | Phase 4 + 5                      |
| 8     | UI Polish & UX                    | Loading states, errors, responsive design, empty states| Medium           | Phase 6                          |
| 9     | Testing & Verification            | Integration test cases, manual flows, multi-user test  | Medium           | All previous                     |
| 10    | Documentation & Final Cleanup     | README, CLAUDE.md updates, final spec alignment        | Small            | All previous                     |

## 2. Detailed Step-by-Step Plan

### Phase 1 – Setup & Foundation

1. Create monorepo folder structure
2. Initialize Next.js (frontend/) with App Router + TypeScript + Tailwind
3. Initialize FastAPI project (backend/) with basic structure
4. Set up .env file (example values + .env.example)
5. Configure docker-compose.yml (frontend, backend, optional db proxy if needed)
6. Add root CLAUDE.md + frontend/CLAUDE.md + backend/CLAUDE.md
7. Configure .spec-kit/config.yaml (phases, directories)

### Phase 2 – Database & Models

1. Write /specs/database/schema.md
2. Set up Neon PostgreSQL connection string in .env
3. Implement db.py (engine, session, get_db dependency)
4. Define SQLModel models:
   - Task model (with user_id foreign key)
   - (users table managed by Better Auth – do not redefine)
5. Create initial migration / table creation script (or use auto-create for dev)

### Phase 3 – Authentication – Backend

1. Write /specs/features/authentication.md
2. Implement JWT verification:
   - Read BETTER_AUTH_SECRET from env
   - Dependency: get_current_user → returns user info or raises 401
   - Protect all task routes with Depends(get_current_user)
3. Add middleware or dependency to attach user to request.state

### Phase 4 – Authentication – Frontend

1. Install & configure Better Auth in Next.js
2. Set up same BETTER_AUTH_SECRET in frontend .env
3. Create auth pages:
   - /login
   - /signup
   - /logout action
4. Create protected layout / middleware to redirect unauthenticated users
5. Store session/token and make it available to API calls

### Phase 5 – Core Task CRUD – Backend

1. Write /specs/api/rest-endpoints.md
2. Implement routes/tasks.py:
   - POST /api/tasks
   - GET /api/tasks (with optional query params: status, sort)
   - GET /api/tasks/{task_id}
   - PUT /api/tasks/{task_id}
   - DELETE /api/tasks/{task_id}
   - PATCH /api/tasks/{task_id}/complete
3. Enforce ownership in every operation (check task.user_id == current_user.id)
4. Use Pydantic response models
5. Handle 401, 403, 404 correctly

### Phase 6 – Core Task CRUD – Frontend

1. Create lib/api.ts – type-safe API client with auth header
2. Build main screens:
   - Dashboard / tasks page (list all tasks)
   - Create task form (modal or separate page)
   - Edit task form
   - Delete confirmation
   - Toggle complete button/checkbox
3. Use server components where possible
4. Handle loading, error, empty states

### Phase 7 – API Client & Auth Integration

1. Make sure every API call includes Authorization header
2. Handle 401 → redirect to login
3. Handle 403/404 → user-friendly message

### Phase 8 – UI Polish & UX

1. Add loading skeletons
2. Add toast notifications (sonner, react-hot-toast, etc.)
3. Improve responsive design (mobile + desktop)
4. Add basic empty state UI
5. Consistent styling & spacing

### Phase 9 – Testing & Verification

1. Write /specs/integration-tests.md or similar
2. Manual test scenarios:
   - User A creates tasks → User B cannot see them
   - Invalid token → 401
   - Ownership violation → 403
   - CRUD full cycle for one user
3. Basic automated ideas (optional):
   - Playwright E2E
   - pytest for backend endpoints

### Phase 10 – Documentation & Final Cleanup

1. Update README.md
2. Update root CLAUDE.md & sub CLAUDE.md files
3. Make sure all specs reference each other correctly
4. Final alignment check with /specs/constitution.md & /specs/specify.md

## 3. Priority Order Recommendation (Most Critical Path)

1. Setup + Database + Models
2. Backend Auth (JWT verification)
3. Task CRUD Backend
4. Frontend Auth (login/signup)
5. API Client
6. Task List + CRUD UI
7. Polish + Testing

## 4. Success Criteria for Phase 2 Completion

- A user can sign up / log in / log out
- Only logged-in users can access task features
- Each user sees **only their own tasks**
- Full CRUD + complete toggle works
- No way to access another user's tasks
- Application runs via docker-compose or separate dev servers
- UI is usable on desktop and mobile
- No crashes on common error cases

End of Phase 2 Development Plan

Agents should follow this sequence and cross-reference:
- /specs/constitution.md
- /specs/specify.md
- /specs/plan.md
```

## Response snapshot

Completed comprehensive implementation planning for the Full-Stack Todo Web Application with:

1. Created detailed implementation plan at /specs/1-full-stack-todo-app/plan/plan.md with technical context and constitution compliance check
2. Researched and documented technical decisions in /specs/1-full-stack-todo-app/research.md including Better Auth + FastAPI integration, Neon PostgreSQL configuration, and JWT secret management
3. Designed comprehensive data model for Task entity in /specs/1-full-stack-todo-app/data-model.md with proper relationships and validation rules
4. Created OpenAPI specification for task endpoints in /specs/1-full-stack-todo-app/contracts/tasks.yaml with complete schema definitions
5. Developed quickstart guide in /specs/1-full-stack-todo-app/quickstart.md with setup instructions and testing procedures

All deliverables align with the constitution principles and technical requirements specified in the original plan.

## Outcome

- ✅ Impact: Created complete implementation plan with all foundational artifacts
- 🧪 Tests: Defined testing procedures and validation criteria
- 📁 Files: Created plan, research, data model, contracts, and quickstart documentation
- 🔁 Next prompts: Proceed to task execution with /sp.tasks
- 🧠 Reflection: Successfully completed planning phase with comprehensive technical specifications

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task execution based on created planning artifacts