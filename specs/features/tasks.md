# Feature: Task Management

## Purpose
Enables authenticated users to perform full CRUD operations on their personal todo tasks with secure data isolation.

## User Stories
- As an authenticated user, I want to create new tasks with title and description so that I can add items to my todo list
- As an authenticated user, I want to view all my tasks in a list so that I can see what needs to be done
- As an authenticated user, I want to update task details including completion status so that I can modify and track progress on tasks
- As an authenticated user, I want to delete tasks so that I can remove completed or unwanted items from my list
- As an authenticated user, I want to mark tasks as complete or incomplete so that I can track my productivity

## Acceptance Criteria
### Task Creation
- Given user is authenticated with valid JWT token
- When user sends POST /api/tasks with title (1-200 chars) and optional description
- Then system creates task with unique ID, sets user_id to authenticated user, completed=false, timestamps, and returns 201 with task data

### Task Listing
- Given user is authenticated
- When user sends GET /api/tasks
- Then system returns 200 with array of user's tasks ordered by creation date (newest first)

### Task Retrieval
- Given user is authenticated and owns the task
- When user sends GET /api/tasks/{id}
- Then system returns 200 with complete task data

### Task Update
- Given user is authenticated and owns the task
- When user sends PUT /api/tasks/{id} with updated title, description, or completed status
- Then system updates the task, sets updated_at timestamp, and returns 200 with updated task data

### Task Deletion
- Given user is authenticated and owns the task
- When user sends DELETE /api/tasks/{id}
- Then system permanently removes the task and returns 204

### Task Completion Toggle
- Given user is authenticated and owns the task
- When user sends PUT /api/tasks/{id} with completed=true/false
- Then system updates completion status and returns 200 with updated task

### Unauthorized Access
- Given user is not authenticated
- When user attempts any task operation
- Then system returns 401 Unauthorized

### Task Not Found
- Given user is authenticated but task doesn't exist or belongs to another user
- When user sends GET/PUT/DELETE /api/tasks/{id}
- Then system returns 404 Not Found

## Edge Cases & Constraints
- Title minimum length: 1 character → validation error if empty
- Title maximum length: 200 characters → validation error if exceeded
- Description: optional, no length limit but reasonable max (e.g., 1000 chars)
- Task ID: must be integer, positive → 400 Bad Request for invalid format
- User can only access tasks where user_id matches their authenticated user ID → 404 for other users' tasks
- Completed status: boolean only (true/false) → 400 for invalid values
- Timestamps: automatically set on create/update, cannot be manually set
- Concurrent updates: last write wins (no optimistic locking for MVP)

## Business Rules
- Tasks are private: users can only see/modify their own tasks
- Task ownership determined by user_id foreign key to authenticated user
- Completed tasks remain in list until explicitly deleted
- No task sharing or collaboration features
- No task categories, priorities, or due dates (future features)
- All operations require valid authentication
- Data validation occurs at API level with clear error messages

## Related Specs
- @specs/features/authentication.md
- @specs/database/schema.md
- @specs/features/integration-tests.md

## Open Questions / Decisions Needed
- Should task listing support filtering/sorting beyond creation date?
- What are the exact error message formats for validation failures?
- Is there a need for task archiving instead of deletion?
- Should completed tasks be visually distinguished in the UI?</content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\specs\features\tasks.md