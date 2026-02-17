# Data Model: Full-Stack Todo Web Application

## Overview

The data model for the Todo Web Application leverages Better Auth for user management and implements a custom Task model with user ownership.

## Entities

### Task Entity

The Task entity represents a user's todo item with full CRUD capabilities and ownership tracking.

**Fields:**
- `id`: integer (Primary Key, Auto-increment)
  - Purpose: Unique identifier for each task
  - Constraints: Not null, auto-generated
- `user_id`: string (Foreign Key)
  - Purpose: Links task to the user who created it
  - Constraints: Not null, references Better Auth user.id
  - Note: Used for authorization checks to ensure user isolation
- `title`: string (max 200 characters)
  - Purpose: Brief description of the task
  - Constraints: Not null, max 200 chars
  - Validation: Required field, min 1 character
- `description`: text (nullable)
  - Purpose: Detailed description of the task
  - Constraints: Optional, can be null
  - Validation: Max reasonable length (handled by database text type)
- `completed`: boolean
  - Purpose: Tracks completion status of the task
  - Constraints: Not null, default false
  - Values: true (completed) or false (pending)
- `created_at`: timestamp with timezone
  - Purpose: Records when the task was created
  - Constraints: Not null, auto-generated
  - Default: Current timestamp at creation
- `updated_at`: timestamp with timezone
  - Purpose: Records last modification time
  - Constraints: Not null, auto-generated
  - Default: Current timestamp at creation and update

**Relationships:**
- One-to-Many: User (via Better Auth) → Tasks
  - Each user can have multiple tasks
  - Each task belongs to exactly one user
  - Enforced by user_id foreign key constraint

**Validation Rules:**
1. Title must be 1-200 characters
2. Description, if provided, must be valid text
3. Completed status is always boolean
4. user_id must correspond to a valid Better Auth user
5. Only the task owner can modify/delete the task

### Better Auth User Integration

The user data is managed by Better Auth and follows their standard schema:

**Reference Fields (from Better Auth):**
- `id`: string - Unique user identifier
- `email`: string - User's email address
- `name`: string (optional) - User's name

**Authorization:**
- All task operations require valid JWT authentication
- Task access is restricted to the owning user (user_id check)
- No cross-user access is allowed

## Database Indexes

To optimize query performance, the following indexes are implemented:

1. **user_id index** (B-tree)
   - Purpose: Optimize queries filtering by user
   - Usage: All get tasks for user operations
   - Performance: Significantly improves user-specific queries

2. **completed index** (B-tree)
   - Purpose: Optimize queries filtering by completion status
   - Usage: Filtering tasks by completed/pending status
   - Performance: Improves status-based filtering

3. **(user_id, completed) composite index** (B-tree)
   - Purpose: Optimize queries filtering by both user and status
   - Usage: Get pending/completed tasks for a user
   - Performance: Optimizes common combined queries

## State Transitions

Tasks have a simple binary state for completion:

**State Diagram:**
```
[Pending] <-- Toggle --> [Completed]
```

**Transitions:**
- Pending → Completed: When user marks task as complete
- Completed → Pending: When user unmarks task as complete
- Both transitions require authentication and ownership verification

## Data Integrity

1. **Referential Integrity:**
   - Foreign key constraint ensures user_id references valid user
   - Prevents orphaned tasks

2. **Authorization Integrity:**
   - Application-level checks ensure only owners can access tasks
   - Prevents unauthorized access through direct API calls

3. **Input Validation:**
   - All inputs are validated at API and model level
   - Prevents invalid data from entering the system