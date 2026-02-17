# Tasks: Todo Web App Architecture

**Input**: Design documents from `/specs/architecture.md`
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
  IMPORTANT: The tasks below are ACTUAL tasks based on the architecture.md document.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure with monorepo layout in apps/ and packages/
- [ ] T002 Initialize Next.js frontend in apps/client with TypeScript
- [ ] T003 Initialize FastAPI backend in apps/server with Python dependencies
- [ ] T004 [P] Initialize shared packages for types and utilities in packages/
- [ ] T005 Configure ESLint and Prettier for frontend code formatting
- [ ] T006 Configure linting and formatting for Python backend code
- [ ] T007 Set up package management with appropriate tools (bun/pnpm for frontend, pip/poetry for backend)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T008 Setup database schema and migrations framework using SQLAlchemy and Alembic in apps/server/
- [ ] T009 [P] Implement Better Auth authentication framework in apps/client and apps/server
- [ ] T010 [P] Setup Neon database connection configuration in apps/server/database/
- [ ] T011 Create JWT validation middleware in apps/server/middleware/
- [ ] T012 Configure API routing structure and base middleware in apps/server/api/
- [ ] T013 Create base user and task models in apps/server/models/
- [ ] T014 Configure error handling and logging infrastructure in apps/server/
- [ ] T015 Setup environment configuration management in apps/server/
- [ ] T016 Configure CORS and security headers for Next.js frontend in apps/client/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Task Management (Priority: P1) 🎯 MVP

**Goal**: Allow authenticated users to create, view, update, and delete tasks

**Independent Test**: User can successfully perform CRUD operations on tasks after authentication

### Implementation for User Story 1

- [ ] T017 [P] Create Task model in apps/server/models/task.py
- [ ] T018 [P] Create Task schema in apps/server/schemas/task.py
- [ ] T019 Create Task service in apps/server/services/task_service.py
- [ ] T020 Implement GET /api/tasks endpoint in apps/server/api/tasks.py
- [ ] T021 Implement POST /api/tasks endpoint in apps/server/api/tasks.py
- [ ] T022 Implement PUT /api/tasks/{id} endpoint in apps/server/api/tasks.py
- [ ] T023 Implement DELETE /api/tasks/{id} endpoint in apps/server/api/tasks.py
- [ ] T024 Create task management components in apps/client/components/Task/
- [ ] T025 Implement task list page in apps/client/pages/tasks/index.tsx
- [ ] T026 Implement task creation form in apps/client/components/Task/CreateTask.tsx
- [ ] T027 Implement task editing functionality in apps/client/components/Task/EditTask.tsx
- [ ] T028 Add authentication check to task routes in apps/client

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Authentication Flow (Priority: P2)

**Goal**: Enable user registration, login, and session management with JWT

**Independent Test**: Users can register, login, logout, and maintain sessions using JWT tokens

### Implementation for User Story 2

- [ ] T029 [P] Create User model in apps/server/models/user.py
- [ ] T030 [P] Create User schemas in apps/server/schemas/user.py
- [ ] T031 Implement authentication service in apps/server/services/auth_service.py
- [ ] T032 Implement POST /api/auth/register endpoint in apps/server/api/auth.py
- [ ] T033 Implement POST /api/auth/login endpoint in apps/server/api/auth.py
- [ ] T034 Implement POST /api/auth/logout endpoint in apps/server/api/auth.py
- [ ] T035 Implement GET /api/auth/me endpoint in apps/server/api/auth.py
- [ ] T036 Configure Better Auth in apps/client with Next.js middleware
- [ ] T037 Create authentication components in apps/client/components/Auth/
- [ ] T038 Implement login page in apps/client/pages/login.tsx
- [ ] T039 Implement registration page in apps/client/pages/register.tsx
- [ ] T040 Add protected routes for authenticated users in apps/client

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Task Filtering and Organization (Priority: P3)

**Goal**: Allow users to filter, sort, and organize tasks with categories or tags

**Independent Test**: Users can filter tasks by status, date, or other criteria

### Implementation for User Story 3

- [ ] T041 [P] Extend Task model with category/tag fields in apps/server/models/task.py
- [ ] T042 [P] Create Category/Tag model in apps/server/models/category.py
- [ ] T043 Update Task service with filtering capabilities in apps/server/services/task_service.py
- [ ] T044 Implement advanced GET /api/tasks with query parameters in apps/server/api/tasks.py
- [ ] T045 Create task filter components in apps/client/components/Task/Filter/
- [ ] T046 Implement task categorization UI in apps/client/components/Task/
- [ ] T047 Add task status management in apps/client/components/Task/
- [ ] T048 Update task list to support filtering and sorting in apps/client/pages/tasks/index.tsx

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Security and Performance (Priority: P4)

**Goal**: Implement security measures and performance optimizations

**Independent Test**: API endpoints are secured, database queries are optimized, and performance is acceptable

### Implementation for User Story 4

- [ ] T049 Implement rate limiting for authentication endpoints in apps/server/middleware/
- [ ] T050 Add input validation and sanitization using Pydantic schemas in apps/server/
- [ ] T051 Implement database query optimization with proper indexing in apps/server/models/
- [ ] T052 Add security middleware for headers and CSRF protection in apps/server/middleware/
- [ ] T053 Implement caching for frequently accessed data in apps/server/services/
- [ ] T054 Add audit logging for sensitive operations in apps/server/
- [ ] T055 Performance testing and optimization of API endpoints in apps/server/

**Checkpoint**: All user stories including security and performance enhancements are functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T056 [P] Documentation updates for API endpoints in apps/server/docs/
- [ ] T057 [P] Documentation updates for frontend components in apps/client/README.md
- [ ] T058 Code cleanup and refactoring across both frontend and backend
- [ ] T059 Performance optimization across all stories
- [ ] T060 [P] Additional unit tests in apps/server/tests/ and apps/client/tests/
- [ ] T061 Security hardening and vulnerability scanning
- [ ] T062 Integration testing between frontend and backend
- [ ] T063 Deploy to staging environment and validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Builds on User Story 1
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Affects all stories

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Create Task model in apps/server/models/task.py"
Task: "Create Task schema in apps/server/schemas/task.py"

# Launch all API endpoints for User Story 1 together:
Task: "Implement GET /api/tasks endpoint in apps/server/api/tasks.py"
Task: "Implement POST /api/tasks endpoint in apps/server/api/tasks.py"
Task: "Implement PUT /api/tasks/{id} endpoint in apps/server/api/tasks.py"
Task: "Implement DELETE /api/tasks/{id} endpoint in apps/server/api/tasks.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
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