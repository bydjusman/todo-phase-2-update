---
id: 8
title: full-stack-todo-app-spec
stage: spec
date: 2026-02-16
surface: agent
model: if/qwen3-coder-plus
feature: full-stack-todo-app
branch: 1-full-stack-todo-app
user: User
command: /sp.specify
labels: [specification, todo-app, authentication, full-stack]
links:
  spec: /specs/1-full-stack-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-full-stack-todo-app/spec.md
 - specs/1-full-stack-todo-app/checklists/requirements.md
tests:
---

## Prompt

```
# /specs/specify.md
# Phase 2 – Full-Stack Todo Web Application Specification
(High-Level Project Spec – Single Source of Truth)

Version: 1.0
Phase: II – Multi-user Web Application with Persistent Storage & Authentication
Status: Active
Related documents:
- /specs/constitution.md               → binding rules & laws
- /specs/overview.md                    → project vision
- /specs/features/task-crud.md          → core feature
- /specs/features/authentication.md     → auth feature
- /specs/api/rest-endpoints.md          → API contract
- /specs/database/schema.md             → data model
- /specs/architecture.md                → system design

## 1. Project Goal (Phase 2)

Transform the Phase 1 console-based Todo application into a **modern, secure, multi-user web application** with:

- Persistent storage in real database
- User authentication & ownership isolation
- Responsive browser interface
- RESTful backend API
- Clean separation between frontend & backend

**Must be completed in Phase 2 (no chatbot yet – that is Phase 3)**

## 2. Non-Functional Requirements (Mandatory)

| Requirement              | Specification                                                                 |
|--------------------------|-------------------------------------------------------------------------------|
| Multi-user isolation     | Each user can only see, create, update, delete **their own** tasks            |
| Authentication           | Required for all task operations                                              |
| Authorization            | Enforced on every request – 403 if accessing another user's data              |
| Data persistence         | Neon Serverless PostgreSQL – survives restarts                                |
| Frontend framework       | Next.js 16+ (App Router), TypeScript, Tailwind CSS                            |
| Backend framework        | FastAPI + SQLModel                                                            |
| Auth mechanism           | Better Auth (frontend) → issues JWT → backend verifies JWT                    |
| JWT handling             | Stateless, secret shared via env var BETTER_AUTH_SECRET                       |
| API style                | RESTful, resource-based, clean paths (/api/tasks, not /api/{userId}/tasks)   |
| Error responses          | Standard HTTP status + JSON { message, detail?, code? }                       |
| UI                       | Responsive, mobile-friendly, loading states, error messages                  |
| Security                 | No hard-coded secrets, input validation, ownership checks                    |
| Type safety              | 100% TypeScript (frontend), full type hints + Pydantic (backend)              |
| Styling                  | Tailwind CSS only – no inline styles, no CSS modules                          |

## 3. Core Functional Scope (Phase 2)

### Must-have features

1. **User Authentication**
   - Sign up (email + password)
   - Sign in
   - Sign out
   - Protected routes (redirect to login if not authenticated)
   - JWT issued on login → sent in every API request

2. **Task CRUD + Complete Toggle**
   - Create task (title required, description optional)
   - List all my tasks
   - View single task details
   - Update task (title & description)
   - Delete task
   - Mark task as completed / pending (toggle)

3. **Basic UI Screens**
   - Login / Signup page
   - Dashboard / Task list page
   - Create new task form (modal or page)
   - Edit task form
   - Delete confirmation (simple or modal)

### Nice-to-have (if time allows – not mandatory)

- Filter tasks by status (all / pending / completed)
- Sort tasks (by created date, title)
- Simple search by title
- Task created/updated timestamps display
- Loading skeletons
- Toast notifications for success/error

## 4. API Contract Overview (must match /specs/api/rest-endpoints.md)

All endpoints under `/api/`
All require `Authorization: Bearer <jwt>`

| Method | Endpoint                | Description                     | Auth required | Response status |
|--------|-------------------------|---------------------------------|---------------|-----------------|
| POST   | /api/tasks              | Create new task                 | Yes           | 201             |
| GET    | /api/tasks              | List my tasks                   | Yes           | 200             |
| GET    | /api/tasks/{task_id}    | Get single task                 | Yes           | 200 / 404       |
| PUT    | /api/tasks/{task_id}    | Update task                     | Yes           | 200 / 404       |
| DELETE | /api/tasks/{task_id}    | Delete task                     | Yes           | 204 / 404       |
| PATCH  | /api/tasks/{task_id}/complete | Toggle completed status   | Yes           | 200 / 404       |

Query params example (GET /api/tasks):
- ?status=pending
- ?sort=created_at
- ?sort=-title (descending)

## 5. Data Model Highlights (must match /specs/database/schema.md)

**users** table — managed by Better Auth
- id (string / UUID)
- email
- name (optional)

**tasks** table
- id (integer, PK, auto-increment)
- user_id (string, FK → users.id)
- title (string, not null, max 200)
- description (text, nullable)
- completed (boolean, default false)
- created_at (timestamp, auto)
- updated_at (timestamp, auto)

Indexes:
- user_id
- completed
- (user_id, completed) composite

## 6. Important Constraints & Decisions

- **No user_id in URL path** → security & cleaner design
- **JWT secret** must be the same in frontend (Better Auth) & backend
- **Database connection** via environment variable DATABASE_URL (Neon)
- **Frontend API calls** must attach JWT automatically
- **Backend must reject** requests without valid JWT (401)
- **Backend must reject** requests for tasks not belonging to user (403)
- **No global admin view** in Phase 2
- **No password reset / email verification** required in Phase 2

## 7. Acceptance Criteria – Phase 2 Done When…

1. A new user can sign up and sign in
2. After login, user sees only their own tasks (empty list is ok)
3. User can create, read, update, delete, toggle completion of tasks
4. User 1 cannot see or modify User 2's tasks
5. Logout works and protected pages redirect to login
6. Application runs with `docker-compose up` or separate terminals
7. No crashes on invalid input / missing auth
8. UI is usable on mobile & desktop
9. All code follows /specs/constitution.md rules

## 8. Out of Scope for Phase 2

- Chatbot / AI features (Phase 3)
- Password reset / forgot password
- Social login (Google, GitHub)
- Task categories / tags / priority / due dates
- File attachments
- Notifications
- Admin dashboard
- Rate limiting / advanced security

End of high-level specification.

Agents must always cross-reference this file together with /specs/constitution.md before starting any implementation.
```

## Response snapshot

Created comprehensive specification document for the Full-Stack Todo Web Application at /specs/1-full-stack-todo-app/spec.md with:

- Complete feature overview aligned with Phase 2 requirements
- Detailed user scenarios for new user registration, returning users, and multi-user isolation
- Functional requirements covering authentication, task management, API endpoints, UI, and data persistence
- Non-functional requirements for security, performance, and usability
- Measurable success criteria with quantitative and qualitative metrics
- Key entities definition for User and Task
- Clear scope boundaries with in/out of scope items
- Dependencies and assumptions documentation
- Quality checklist validation confirming specification readiness

## Outcome

- ✅ Impact: Created complete feature specification aligned with project requirements
- 🧪 Tests: Specification includes testing approach and validation criteria
- 📁 Files: Created spec.md and requirements.md checklist
- 🔁 Next prompts: Planning phase with /sp.plan or clarification with /sp.clarify
- 🧠 Reflection: Successfully transformed high-level requirements into detailed specification with measurable outcomes

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning implementation based on this specification