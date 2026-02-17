# Task CRUD Feature Specification

## Feature Overview

The Task CRUD (Create, Read, Update, Delete) feature enables authenticated users to manage their personal todo tasks. Each user has complete control over their own tasks, with proper authorization checks to prevent cross-user access.

## User Stories

### User Story 1 (P1) - Create Task
**As an** authenticated user,
**I want** to create new tasks with a title and optional description,
**So that** I can keep track of things I need to do.

**Acceptance Criteria:**
- User can provide a task title (required, 1-200 characters)
- User can optionally provide a task description
- Task is created with default "completed" status of false
- Task is associated with the authenticated user
- Task creation returns the complete task object with all fields
- System prevents creation without authentication

### User Story 2 (P1) - Read Tasks
**As an** authenticated user,
**I want** to view all my tasks,
**So that** I can see what I need to do and what I've completed.

**Acceptance Criteria:**
- User can retrieve all their tasks in a single request
- Tasks are returned with ID, title, description, completion status, and timestamps
- User can only retrieve their own tasks (authorization enforced)
- Response includes pagination, filtering, and sorting options
- Empty list returned if user has no tasks

### User Story 3 (P1) - Update Task
**As an** authenticated user,
**I want** to update my tasks (title, description, completion status),
**So that** I can keep my todo list accurate and mark tasks as completed.

**Acceptance Criteria:**
- User can update task title (1-200 characters)
- User can update task description (optional)
- User can toggle completion status
- System only allows updating tasks owned by the authenticated user
- Updated task is returned with all fields
- Partial updates are supported (PATCH method)

### User Story 4 (P1) - Delete Task
**As an** authenticated user,
**I want** to delete tasks I no longer need,
**So that** I can maintain a clean and relevant todo list.

**Acceptance Criteria:**
- User can delete their own tasks
- System prevents deletion of tasks owned by other users
- Deletion returns appropriate status (204 No Content)
- Deleted task is no longer accessible

## Functional Requirements

### FR-TASK-001: Create Task
**REQ-FR-TASK-001.1**: The system SHALL accept POST requests to `/api/tasks` with title and optional description
**REQ-FR-TASK-001.2**: The system SHALL validate that title is 1-200 characters
**REQ-FR-TASK-001.3**: The system SHALL set completion status to false by default
**REQ-FR-TASK-001.4**: The system SHALL associate the task with the authenticated user
**REQ-FR-TASK-001.5**: The system SHALL return HTTP 201 Created with the new task object

### FR-TASK-002: Read Tasks
**REQ-FR-TASK-002.1**: The system SHALL accept GET requests to `/api/tasks`
**REQ-FR-TASK-002.2**: The system SHALL return only tasks belonging to the authenticated user
**REQ-FR-TASK-002.3**: The system SHALL support query parameters: status, sort, page, limit
**REQ-FR-TASK-002.4**: The system SHALL return HTTP 200 with task array and metadata

### FR-TASK-003: Get Single Task
**REQ-FR-TASK-003.1**: The system SHALL accept GET requests to `/api/tasks/{id}`
**REQ-FR-TASK-003.2**: The system SHALL return only tasks belonging to the authenticated user
**REQ-FR-TASK-003.3**: The system SHALL return HTTP 404 if task doesn't exist
**REQ-FR-TASK-003.4**: The system SHALL return HTTP 403 if user doesn't own the task

### FR-TASK-004: Update Task
**REQ-FR-TASK-004.1**: The system SHALL accept PUT requests to `/api/tasks/{id}` with full task data
**REQ-FR-TASK-004.2**: The system SHALL accept PATCH requests to `/api/tasks/{id}` with partial updates
**REQ-FR-TASK-004.3**: The system SHALL validate that the authenticated user owns the task
**REQ-FR-TASK-004.4**: The system SHALL return HTTP 200 with updated task object

### FR-TASK-005: Delete Task
**REQ-FR-TASK-005.1**: The system SHALL accept DELETE requests to `/api/tasks/{id}`
**REQ-FR-TASK-005.2**: The system SHALL validate that the authenticated user owns the task
**REQ-FR-TASK-005.3**: The system SHALL return HTTP 204 No Content
**REQ-FR-TASK-005.4**: The system SHALL prevent access to the deleted task after deletion

### FR-TASK-006: Toggle Completion
**REQ-FR-TASK-006.1**: The system SHALL accept PATCH requests to `/api/tasks/{id}` to toggle completion status
**REQ-FR-TASK-006.2**: The system SHALL validate that the authenticated user owns the task
**REQ-FR-TASK-006.3**: The system SHALL return HTTP 200 with updated task object

## Non-Functional Requirements

### NFR-TASK-001: Security
**REQ-NFR-TASK-001.1**: The system SHALL enforce authentication for all task operations
**REQ-NFR-TASK-001.2**: The system SHALL enforce authorization to prevent cross-user access
**REQ-NFR-TASK-001.3**: The system SHALL return HTTP 401 for unauthenticated requests
**REQ-NFR-TASK-001.4**: The system SHALL return HTTP 403 for unauthorized access attempts

### NFR-TASK-002: Performance
**REQ-NFR-TASK-002.1**: The system SHALL respond to task requests within 1 second under normal load
**REQ-NFR-TASK-002.2**: The system SHALL support pagination for large task lists
**REQ-NFR-TASK-002.3**: The system SHALL implement database indexing for efficient queries

### NFR-TASK-003: Data Integrity
**REQ-NFR-TASK-003.1**: The system SHALL validate all input according to defined constraints
**REQ-NFR-TASK-003.2**: The system SHALL maintain referential integrity between users and tasks
**REQ-NFR-TASK-003.3**: The system SHALL handle errors gracefully without data corruption

## API Contract

### POST /api/tasks
**Description**: Create a new task for the authenticated user
**Auth Required**: Yes
**Request Body**:
```json
{
  "title": "string, required, max 200 chars",
  "description": "string, optional",
  "completed": "boolean, optional, default false"
}
```
**Response 201**:
```json
{
  "data": {
    "id": 1,
    "user_id": "string",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
}
```

### GET /api/tasks
**Description**: Get all tasks for the authenticated user
**Auth Required**: Yes
**Query Parameters**:
- status: "all" | "pending" | "completed" (default: "all")
- sort: "created_at" | "-created_at" | "title" | "-title" (default: "-created_at")
- page: integer (default: 1)
- limit: integer (default: 20)
**Response 200**:
```json
{
  "data": [...],
  "meta": {
    "total": 42,
    "page": 1,
    "limit": 20,
    "total_pages": 3
  }
}
```

### GET /api/tasks/{id}
**Description**: Get a specific task
**Auth Required**: Yes
**Response 200**:
```json
{
  "data": { ...task object... }
}
```
**Response 404**: If task not found
**Response 403**: If user doesn't own the task

### PUT /api/tasks/{id}
**Description**: Update a task completely
**Auth Required**: Yes
**Response 200**: With updated task

### PATCH /api/tasks/{id}
**Description**: Update a task partially
**Auth Required**: Yes
**Response 200**: With updated task

### DELETE /api/tasks/{id}
**Description**: Delete a task
**Auth Required**: Yes
**Response 204**: On successful deletion

## Data Model

### Task Entity
- **id**: integer (Primary Key, Auto-increment)
- **user_id**: string (Foreign Key to user, required)
- **title**: string (1-200 characters, required)
- **description**: string (nullable)
- **completed**: boolean (default: false)
- **created_at**: timestamp (auto-generated)
- **updated_at**: timestamp (auto-generated)

## Error Handling

### Standard Error Response Format
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Error description"
  }
}
```

### Common Error Codes
- **AUTH_REQUIRED**: For 401 responses when authentication is missing
- **FORBIDDEN**: For 403 responses when user doesn't have access
- **NOT_FOUND**: For 404 responses when resource doesn't exist
- **VALIDATION_ERROR**: For 422 responses when input validation fails
- **SERVER_ERROR**: For 5xx responses

## Success Criteria

1. 100% of authenticated users can create, read, update, and delete their own tasks
2. 0% of users can access tasks belonging to other users
3. All API endpoints respond within 1 second under normal load
4. All input is properly validated according to specified constraints
5. All operations properly authenticate and authorize the requesting user