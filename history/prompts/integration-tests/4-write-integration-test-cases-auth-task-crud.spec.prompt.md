---
id: 4
title: Write Integration Test Cases for Auth and Task CRUD
stage: spec
date: 2026-02-16
surface: agent
model: Grok
feature: integration-tests
branch: main
user: user
command: 
labels: ["integration", "tests", "authentication", "crud"]
links:
  spec: 
  ticket: 
  adr: 
  pr: 
files:
 - specs/features/integration-tests.md
tests:
 - TC001: User Signup, Task Creation, and Task Listing
 - TC002: User Isolation - Cannot Access Other Users' Tasks
 - TC003: Invalid/Expired JWT Token Handling
 - TC004: Task Deletion and Verification
 - TC005: Task Completion Toggle
---

## Prompt

You are the Integration Tester Agent.

Write integration test cases for authentication + task CRUD.

Cover:
- Signup → create task → list tasks (only own)
- Login as user2 → cannot see user1 tasks
- Invalid/expired JWT → 401
- Delete task → 204 & gone on next GET
- Toggle complete

Format as markdown checklist + expected behavior.

## Response snapshot

Created comprehensive integration test cases in /specs/features/integration-tests.md covering authentication flows and task CRUD operations with detailed steps and expected behaviors.

## Outcome

- ✅ Impact: Defined complete integration test suite for auth + task functionality
- 🧪 Tests: 5 core test cases with additional recommended scenarios
- 📁 Files: Created specs/features/integration-tests.md
- 🔁 Next prompts: Implement the test cases in apps/server/tests/
- 🧠 Reflection: Successfully covered all requested scenarios with proper isolation and security testing

## Evaluation notes (flywheel)

- Failure modes observed: 
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): 
- Next experiment (smallest change to try): </content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\history\prompts\integration-tests\4-write-integration-test-cases-auth-task-crud.spec.prompt.md