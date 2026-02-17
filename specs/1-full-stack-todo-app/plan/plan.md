# Implementation Plan: Full-Stack Todo Web Application

## Technical Context

**Feature:** Full-Stack Todo Web Application with Authentication and Persistent Storage
**Tech Stack:**
- Frontend: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- Backend: FastAPI, SQLModel, Python
- Authentication: Better Auth + JWT
- Database: Neon Serverless PostgreSQL
- Architecture: Monorepo with separate frontend/backend apps

**Technical Decisions:**
- Use python-jose library to verify Better Auth JWT tokens in FastAPI backend
- Use environment-specific connection strings with conservative pool settings for Neon
- Share BETTER_AUTH_SECRET between frontend and backend via environment variables
- Implement JWT verification middleware with user extraction in FastAPI
- Use SQLModel for database models with proper foreign key relationships

## Constitution Check

Based on `/specs/constitution.md`, this implementation must comply with:

1. **API-First Design**: API contracts documented in specs/api/
2. **Security-First Architecture**: JWT authentication, user data isolation
3. **Test-Driven Development**: All components must have tests
4. **Type Safety & Validation**: TypeScript frontend, Pydantic backend
5. **Performance & Observability**: API responses within performance constraints
6. **Clean Architecture**: Clear separation of concerns

**Gates**:
- ✅ All API endpoints follow RESTful principles with consistent response formats
- ✅ Authentication with JWT required for all task operations
- ✅ User data isolation through user_id foreign key validation
- ✅ All code will be strongly typed using TypeScript/Pydantic
- ✅ Clean architecture principles will separate business logic from infrastructure

## Phase 0: Outline & Research

### Research Tasks

1. **Better Auth + FastAPI Integration**
   - Task: Research how to properly validate Better Auth JWTs in FastAPI backend
   - Task: Determine how to extract user information from Better Auth tokens
   - Task: Find examples of this specific integration pattern

2. **Neon PostgreSQL Configuration**
   - Task: Research optimal connection pool settings for Neon Serverless
   - Task: Understand connection string format and environment variables
   - Task: Find best practices for local vs production database configurations

3. **JWT Secret Management**
   - Task: Research secure ways to share JWT secrets between Better Auth frontend and FastAPI backend
   - Task: Determine if Better Auth generates its own secrets or uses custom ones
   - Task: Find best practices for environment variable management

## Phase 1: Design & Contracts

### Data Model

Based on the feature requirements, the data model includes:

**Task Entity:**
- id: integer (PK, auto-increment)
- user_id: string (FK to Better Auth users.id)
- title: string (max 200 chars, not null)
- description: text (nullable)
- completed: boolean (default false)
- created_at: timestamp (auto-generated)
- updated_at: timestamp (auto-generated)

**Relationships:**
- One User to Many Tasks (user_id → Better Auth user.id)
- Each task belongs to exactly one user
- User can only access their own tasks

### API Contracts

Following the documented API contract in `/specs/api/tasks.md`:

**Task Endpoints:**
- `POST /api/tasks` - Create new task (201 Created)
- `GET /api/tasks` - List user's tasks (200 OK) with query params:
  - status: "all" | "pending" | "completed"
  - sort: "created_at" | "-created_at" | "title" | "-title"
  - page: integer
  - limit: integer
- `GET /api/tasks/{id}` - Get specific task (200 OK, 404 Not Found)
- `PUT /api/tasks/{id}` - Update task (200 OK, 404 Not Found)
- `PATCH /api/tasks/{id}` - Partial update (200 OK, 404 Not Found)
- `DELETE /api/tasks/{id}` - Delete task (204 No Content, 404 Not Found)

**Authentication Endpoints:**
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user

### Quickstart Guide

1. Clone the repository
2. Create `.env` file with:
   - `DATABASE_URL` for Neon PostgreSQL
   - `BETTER_AUTH_SECRET` matching between frontend and backend
   - `NEXT_PUBLIC_API_URL` for frontend API calls
3. Run database migrations
4. Start frontend: `cd apps/client && bun run dev`
5. Start backend: `cd apps/server && python -m uvicorn main:app --reload`
6. Access frontend at `http://localhost:3000`

**Success Criteria for this Phase:**
- [ ] Technical Context completed with no remaining NEEDS CLARIFICATION
- [ ] Constitution Check passes with all compliance gates marked
- [ ] Data model documented with entities and relationships
- [ ] API contracts defined following documented patterns
- [ ] Quickstart guide ready for development