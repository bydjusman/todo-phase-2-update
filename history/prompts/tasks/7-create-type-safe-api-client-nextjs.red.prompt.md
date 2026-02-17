---
id: 7
title: Create Type-Safe API Client for Next.js
stage: red
date: 2026-02-16
surface: agent
model: Grok
feature: tasks
branch: main
user: user
command: 
labels: ["api", "client", "typescript", "nextjs", "authentication"]
links:
  spec: 
  ticket: 
  adr: 
  pr: 
files:
 - apps/client/lib/api.ts
tests:
---

## Prompt

SKILL: Create Type-Safe API Client (Next.js)

You write clean, type-safe API clients for Next.js using fetch or axios.

Rules:
- Create lib/api.ts
- Use TypeScript interfaces for request/response bodies
- Automatically attach Authorization: Bearer ${token} when user is logged in
- Handle 401 → redirect to login
- Handle loading, error, success states
- Use consistent response shape: { data?, error?, meta? }
- Support GET, POST, PUT, PATCH, DELETE
- Add timeout, retry logic (optional but nice)
- Use env variable for API base URL

Preferred pattern:

const api = {
  getTasks: async (params?: GetTasksParams): Promise<Task[]> => {
    const res = await fetchWithAuth(`/api/tasks?${new URLSearchParams(params)}`);
    return handleResponse(res);
  },
  // ...
}

Now write or improve the API client for the todo application.

## Response snapshot

Improved /apps/client/lib/api.ts with comprehensive type-safe API client including authentication, timeout, retry logic, and all CRUD operations for tasks and auth endpoints.

## Outcome

- ✅ Impact: Created robust, type-safe API client with security and error handling
- 🧪 Tests: No tests added yet
- 📁 Files: Updated apps/client/lib/api.ts
- 🔁 Next prompts: Implement React components using this API client
- 🧠 Reflection: Successfully added all required features including auth, timeout, retry, and consistent error handling

## Evaluation notes (flywheel)

- Failure modes observed: 
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): 
- Next experiment (smallest change to try): </content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\history\prompts\tasks\7-create-type-safe-api-client-nextjs.red.prompt.md