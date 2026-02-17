# Tasks: Phase 2 – Todo Full-Stack Web Application

**Input**: Design documents from `/specs/1-full-stack-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Monorepo**: `apps/client/`, `apps/server/`, `packages/` at repository root
- **Frontend**: `apps/client/src/`
- **Backend**: `apps/server/src/`
- **Shared**: `packages/`

<!--
  ============================================================================
  IMPORTANT: The tasks below are based on the specification provided in the user input.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 [P] Initialize monorepo structure with folders frontend/, backend/, specs/, .spec-kit/ in project root
- [X] T002 [P] Set up frontend (Next.js) with TypeScript, Tailwind, ESLint, App Router in apps/client/
- [X] T003 [P] Set up backend (FastAPI) with basic structure in apps/server/main.py
- [X] T004 [P] Create requirements.txt with fastapi, uvicorn, sqlmodel, python-jose[cryptography], passlib[bcrypt], python-multipart in apps/server/
- [X] T005 Create .env.example with DATABASE_URL, BETTER_AUTH_SECRET, NEXT_PUBLIC_API_URL=http://localhost:8000
- [X] T006 Create docker-compose.yml with frontend on port 3000 and backend on port 8000

---

## Phase 2: Specification (Required Documentation)

**Purpose**: Essential specifications that inform implementation

- [X] T007 Write database schema specification to /specs/database/schema.md
- [X] T008 Write authentication feature spec to /specs/features/authentication.md
- [X] T009 Write task CRUD feature spec to /specs/features/task-crud.md
- [X] T010 Write REST API endpoints specification to /specs/api/rest-endpoints.md

---

## Phase 3: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T011 [P] Neon PostgreSQL connection setup in apps/server/database/
- [X] T012 [P] Create SQLModel Task model with user_id, title, description, completed, timestamps in apps/server/models/task.py
- [X] T013 Implement JWT verification dependency with python-jose in apps/server/auth/
- [X] T014 Protect all task routes with authentication in apps/server/api/routes/tasks.py
- [X] T015 Install and configure Better Auth in Next.js frontend apps/client/
- [X] T016 Create auth pages /login, /signup, sign-out action in apps/client/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 4: User Story 1 - User Authentication (Priority: P1) 🎯 MVP

**Goal**: Enable users to register, login, and logout with proper JWT token management

**Independent Test**: User can successfully register, login, and logout with JWT tokens issued and validated

### Implementation for User Story 1

- [X] T017 [P] [US1] Add protected routes middleware to redirect unauthenticated users in apps/client/middleware.ts
- [X] T018 [US1] Create type-safe API client with Authorization header in apps/client/lib/api.ts
- [X] T019 [US1] Implement GET /api/auth/me endpoint in apps/server/api/routes/auth.py
- [X] T020 [US1] Create authentication service in apps/server/services/auth_service.py
- [X] T021 [US1] Handle 401 redirect to login in API client apps/client/lib/api.ts

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 5: User Story 2 - Core Task CRUD (Priority: P1) 🎯 MVP

**Goal**: Allow authenticated users to create, view, update, and delete their tasks

**Independent Test**: User can perform full CRUD operations on their own tasks but not others' tasks

### Implementation for User Story 2

- [X] T022 [P] [US2] Implement POST /api/tasks endpoint in apps/server/api/routes/tasks.py
- [X] T023 [P] [US2] Implement GET /api/tasks endpoint with query params in apps/server/api/routes/tasks.py
- [X] T024 [P] [US2] Implement GET /api/tasks/{id}, PUT, DELETE endpoints in apps/server/api/routes/tasks.py
- [X] T025 [P] [US2] Implement PATCH /api/tasks/{id}/complete endpoint in apps/server/api/routes/tasks.py
- [X] T026 [US2] Enforce ownership checks to ensure users can only access their own tasks in apps/server/api/routes/tasks.py
- [X] T027 [US2] Build task list page with loading/empty/error states in apps/client/app/tasks/page.tsx
- [X] T028 [US2] Build task create & edit form in apps/client/components/task/
- [X] T029 [US2] Add toggle complete and delete actions in apps/client/components/task/

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 6: User Story 3 - Task Organization (Priority: P2)

**Goal**: Enable users to filter, sort, and organize their tasks

**Independent Test**: User can filter and sort their tasks by status, creation date, or title

### Implementation for User Story 3

- [X] T030 [P] [US3] Update GET /api/tasks with filtering, sorting params in apps/server/api/routes/tasks.py
- [X] T031 [US3] Add pagination functionality to task endpoints in apps/server/api/routes/tasks.py
- [X] T032 [US3] Add filtering and sorting controls to task list UI in apps/client/app/tasks/page.tsx
- [X] T033 [US3] Add pagination controls to frontend in apps/client/components/task/

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T034 [P] Add loading skeletons and toast notifications in apps/client/components/
- [X] T035 [P] Write integration test scenarios (manual + optional auto)
- [X] T036 Update README.md with complete setup and usage instructions
- [X] T037 Final consistency check across all specs and implementation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Specification (Phase 2)**: Depends on Setup completion
- **Foundational (Phase 3)**: Depends on Setup and Specification completion - BLOCKS all user stories
- **User Stories (Phase 4+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 3) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 3) - Builds on User Story 1 authentication
- **User Story 3 (P3)**: Can start after Foundational (Phase 3) - Builds on User Story 2

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 3)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 2

```bash
# Launch all backend endpoints for User Story 2 together:
Task: "Implement POST /api/tasks endpoint in apps/server/api/routes/tasks.py"
Task: "Implement GET /api/tasks endpoint with query params in apps/server/api/routes/tasks.py"
Task: "Implement GET /api/tasks/{id}, PUT, DELETE endpoints in apps/server/api/routes/tasks.py"
Task: "Implement PATCH /api/tasks/{id}/complete endpoint in apps/server/api/routes/tasks.py"

# Launch all frontend components for User Story 2 together:
Task: "Build task list page with loading/empty/error states in apps/client/app/tasks/page.tsx"
Task: "Build task create & edit form in apps/client/components/task/"
Task: "Add toggle complete and delete actions in apps/client/components/task/"
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Specification
3. Complete Phase 3: Foundational (CRITICAL - blocks all stories)
4. Complete Phase 4: User Story 1 (Authentication)
5. Complete Phase 5: User Story 2 (Task CRUD)
6. **STOP and VALIDATE**: Test User Stories 1 and 2 together - this is the MVP!
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Specification + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo
3. Add User Story 2 → Test with Story 1 → Deploy/Demo (MVP!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Specification + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Authentication)
   - Developer B: User Story 2 (Task CRUD)
   - Developer C: User Story 3 (Organization)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence