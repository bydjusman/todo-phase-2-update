# API: Tasks

## Base Path
/api/tasks

## Authentication
All endpoints require JWT in Authorization header as `Authorization: Bearer <token>`

## Response Format
All responses follow the envelope pattern:
```json
{
  "data": { ... } | [ ... ],
  "meta": { ... } (optional)
}
```

For errors:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Error description"
  }
}
```

## Endpoints

### GET /api/tasks
Description: Get all tasks for the authenticated user with filtering, sorting, and pagination options

Query params:
- status: "all" | "pending" | "completed" (default: "all")
- sort: "created_at" | "-created_at" | "title" | "-title" (default: "-created_at")
- page: integer (default: 1)
- limit: integer (default: 20, max: 100)

Response 200:
```json
{
  "data": [
    {
      "id": 1,
      "user_id": "user_abc123",
      "title": "Complete project proposal",
      "description": "Write and review the project proposal document",
      "completed": false,
      "created_at": "2023-10-15T14:30:00Z",
      "updated_at": "2023-10-15T14:30:00Z"
    }
  ],
  "meta": {
    "total": 42,
    "page": 1,
    "limit": 20,
    "total_pages": 3
  }
}
```

Status codes:
- 200: Success
- 401: Unauthorized

### POST /api/tasks
Description: Create a new task for the authenticated user

Request body:
```json
{
  "title": "string, required, max 200 chars",
  "description": "string, optional",
  "completed": "boolean, optional, default false"
}
```

Response 201:
```json
{
  "data": {
    "id": 1,
    "user_id": "user_abc123",
    "title": "Complete project proposal",
    "description": "Write and review the project proposal document",
    "completed": false,
    "created_at": "2023-10-15T14:30:00Z",
    "updated_at": "2023-10-15T14:30:00Z"
  }
}
```

Status codes:
- 201: Created
- 400: Invalid request body
- 401: Unauthorized

### GET /api/tasks/{id}
Description: Get a specific task by ID for the authenticated user

Path params:
- id: task ID (integer)

Response 200:
```json
{
  "data": {
    "id": 1,
    "user_id": "user_abc123",
    "title": "Complete project proposal",
    "description": "Write and review the project proposal document",
    "completed": false,
    "created_at": "2023-10-15T14:30:00Z",
    "updated_at": "2023-10-15T14:30:00Z"
  }
}
```

Status codes:
- 200: Success
- 401: Unauthorized
- 403: Task does not belong to user
- 404: Task not found

### PUT /api/tasks/{id}
Description: Update a specific task completely for the authenticated user

Path params:
- id: task ID (integer)

Request body:
```json
{
  "title": "string, required, max 200 chars",
  "description": "string, optional",
  "completed": "boolean, optional"
}
```

Response 200:
```json
{
  "data": {
    "id": 1,
    "user_id": "user_abc123",
    "title": "Updated project proposal",
    "description": "Write and review the project proposal document",
    "completed": true,
    "created_at": "2023-10-15T14:30:00Z",
    "updated_at": "2023-10-15T15:45:00Z"
  }
}
```

Status codes:
- 200: Updated
- 400: Invalid request body
- 401: Unauthorized
- 403: Task does not belong to user
- 404: Task not found

### PATCH /api/tasks/{id}
Description: Partially update a specific task for the authenticated user

Path params:
- id: task ID (integer)

Request body:
```json
{
  "title": "string, optional, max 200 chars",
  "description": "string, optional",
  "completed": "boolean, optional"
}
```

Response 200:
```json
{
  "data": {
    "id": 1,
    "user_id": "user_abc123",
    "title": "Complete project proposal",
    "description": "Updated description",
    "completed": true,
    "created_at": "2023-10-15T14:30:00Z",
    "updated_at": "2023-10-15T15:45:00Z"
  }
}
```

Status codes:
- 200: Updated
- 400: Invalid request body
- 401: Unauthorized
- 403: Task does not belong to user
- 404: Task not found

### DELETE /api/tasks/{id}
Description: Delete a specific task for the authenticated user

Path params:
- id: task ID (integer)

Response 204: No content

Status codes:
- 204: Deleted
- 401: Unauthorized
- 403: Task does not belong to user
- 404: Task not found

## Common Error Responses

400 Bad Request:
```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Request validation failed",
    "details": {
      "field": "error_description"
    }
  }
}
```

401 Unauthorized:
```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required"
  }
}
```

403 Forbidden:
```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "Access denied"
  }
}
```

404 Not Found:
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Resource not found"
  }
}
```

422 Unprocessable Entity:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": {
      "field": "validation_error_description"
    }
  }
}
```