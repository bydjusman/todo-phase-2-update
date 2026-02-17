# Integration Test Cases: Authentication + Task CRUD

## Overview

This document defines integration test cases for the authentication system (Better Auth + JWT) combined with task CRUD operations. Tests verify end-to-end functionality, data isolation, and security.

## Test Environment Setup

- Clean database instance
- Test users: user1@example.com, user2@example.com
- API endpoints available at `/api/*`
- JWT tokens handled via httpOnly cookies

## Test Cases

### TC001: User Signup, Task Creation, and Task Listing (Own Tasks Only)

- [ ] **Test Case: Successful User Registration and Task Management Flow**

  **Description:** Verify that a new user can register, authenticate, create tasks, and only see their own tasks in listings.

  **Preconditions:**
  - No existing user with email `user1@example.com`
  - Clean tasks table

  **Steps:**
  1. Send POST `/api/auth/register` with `{"email": "user1@example.com", "password": "SecurePass123!"}`
  2. Send POST `/api/auth/login` with `{"email": "user1@example.com", "password": "SecurePass123!"}`
  3. Send POST `/api/tasks` with `{"title": "Test Task 1", "description": "Description 1"}`
  4. Send POST `/api/tasks` with `{"title": "Test Task 2", "description": "Description 2"}`
  5. Send GET `/api/tasks`

  **Expected Behavior:**
  - Registration returns 201 with success message
  - Login returns 200 with success message and sets auth cookies
  - Task creation returns 201 with task data (id, user_id matches user1, timestamps set)
  - Task listing returns 200 with array of 2 tasks (only user1's tasks)
  - Each task includes: id, user_id, title, description, completed=false, created_at, updated_at

### TC002: User Isolation - Cannot Access Other Users' Tasks

- [ ] **Test Case: Multi-User Data Isolation**

  **Description:** Ensure users can only access their own tasks, not other users' data.

  **Preconditions:**
  - User1 has 2 tasks from TC001
  - User2 registered and authenticated

  **Steps:**
  1. Send POST `/api/auth/register` with `{"email": "user2@example.com", "password": "SecurePass123!"}`
  2. Send POST `/api/auth/login` with `{"email": "user2@example.com", "password": "SecurePass123!"}`
  3. Send GET `/api/tasks`
  4. Send POST `/api/tasks` with `{"title": "User2 Task", "description": "User2's task"}`
  5. Send GET `/api/tasks`
  6. Switch back to user1 session (login as user1)
  7. Send GET `/api/tasks`

  **Expected Behavior:**
  - User2 registration/login succeeds
  - User2 initial task list returns 200 with empty array []
  - User2 task creation returns 201 with new task
  - User2 task list returns 200 with array of 1 task (only user2's task)
  - User1 task list returns 200 with array of 2 tasks (unchanged, only user1's tasks)

### TC003: Invalid/Expired JWT Token Handling

- [ ] **Test Case: Authentication Failure with Invalid Tokens**

  **Description:** Verify that requests with invalid, missing, or expired JWT tokens are properly rejected.

  **Preconditions:**
  - Valid user session exists
  - Test with various invalid token scenarios

  **Steps:**
  1. Send GET `/api/tasks` without any authentication
  2. Send GET `/api/tasks` with invalid JWT token in Authorization header
  3. Send GET `/api/tasks` with malformed JWT token
  4. Wait for token expiration (or simulate expired token)
  5. Send GET `/api/tasks` with expired token

  **Expected Behavior:**
  - All requests return 401 Unauthorized
  - Response includes error message: "Authentication required" or "Invalid token"
  - No task data is returned
  - Requests are logged for security monitoring

### TC004: Task Deletion and Verification

- [ ] **Test Case: Task Deletion Lifecycle**

  **Description:** Ensure tasks can be deleted and are permanently removed from the system.

  **Preconditions:**
  - User authenticated with at least 1 task

  **Steps:**
  1. Send GET `/api/tasks` to get current task list
  2. Select one task ID from the list
  3. Send DELETE `/api/tasks/{id}`
  4. Send GET `/api/tasks` to verify deletion
  5. Send GET `/api/tasks/{id}` to confirm task is gone

  **Expected Behavior:**
  - Initial GET returns 200 with task list
  - DELETE returns 204 No Content
  - Subsequent GET `/api/tasks` returns 200 with reduced task count
  - GET `/api/tasks/{id}` returns 404 Not Found
  - Task is permanently removed from database

### TC005: Task Completion Toggle

- [ ] **Test Case: Task Status Update**

  **Description:** Verify that task completion status can be toggled between true and false.

  **Preconditions:**
  - User authenticated with at least 1 incomplete task

  **Steps:**
  1. Send GET `/api/tasks` to get current tasks
  2. Select one task with completed=false
  3. Send PUT `/api/tasks/{id}` with `{"completed": true}`
  4. Send GET `/api/tasks/{id}` to verify update
  5. Send PUT `/api/tasks/{id}` with `{"completed": false}`
  6. Send GET `/api/tasks/{id}` to verify toggle back

  **Expected Behavior:**
  - Initial task has completed=false
  - PUT to set completed=true returns 200 with updated task data
  - Task shows completed=true, updated_at timestamp changed
  - PUT to set completed=false returns 200 with updated task data
  - Task shows completed=false, updated_at timestamp changed again
  - Only completion status changes, other fields remain the same

## Additional Test Scenarios (Recommended)

### TC006: Task Update (Title and Description)

- [ ] **Test Case: Task Content Modification**

  **Description:** Ensure task title and description can be updated while preserving other fields.

  **Steps:**
  1. Create a task with title "Original Title"
  2. Update title to "Updated Title" and description to "Updated Description"
  3. Verify only specified fields changed

  **Expected:** Title and description updated, timestamps changed, other fields unchanged.

### TC007: Rate Limiting on Authentication Endpoints

- [ ] **Test Case: Authentication Rate Limiting**

  **Description:** Verify rate limiting prevents brute force attacks on login/register.

  **Steps:**
  1. Send multiple rapid POST `/api/auth/login` with wrong credentials
  2. Verify 429 Too Many Requests after threshold

  **Expected:** Rate limiting activates, requests blocked temporarily.

### TC008: Concurrent Task Operations

- [ ] **Test Case: Concurrent User Operations**

  **Description:** Ensure multiple users can perform operations simultaneously without interference.

  **Steps:**
  1. User1 and User2 both create tasks simultaneously
  2. Both users list their tasks
  3. Verify each sees only their own tasks

  **Expected:** Data isolation maintained under concurrent load.

## Test Execution Notes

- Use test framework like pytest with httpx for API testing
- Mock external services if needed (email verification, etc.)
- Clean up test data between test runs
- Run tests in isolated database transactions
- Include performance assertions for response times (<500ms for simple operations)</content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\specs\features\integration-tests.md