---
id: 3
title: database-schema-spec
stage: spec
date: 2026-02-16
surface: agent
model: if/qwen3-coder-plus
feature: database
branch: master
user: User
command: /sp.tasks
labels: [database, schema, sqlmodel, tasks]
links:
  spec: /specs/database/schema.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/database/schema.md
tests:
---

## Prompt

```
You are the Database Engineer Agent.

Update /specs/database/schema.md and provide SQLModel code for the tasks table.

Requirements:
- user_id: string, foreign key to Better Auth users.id
- title: string, not null, max 200
- description: text, nullable
- completed: bool, default false
- created_at, updated_at timestamps
- Indexes for fast filtering by user & status

Also suggest migration steps if needed.
```

## Response snapshot

Updated the database schema specification document at /specs/database/schema.md to meet the specific requirements:

- Created comprehensive SQLModel definition for the Task class with all required fields
- Implemented user_id as string foreign key to Better Auth users.id
- Set title as string with max length of 200 and not null constraint
- Made description as text field that is nullable
- Set completed as boolean with default value of false
- Included created_at and updated_at timestamp fields
- Added proper indexes for fast filtering by user and status (idx_task_user_id, idx_task_completed, idx_task_user_completed)
- Provided migration steps for database setup
- Included database connection settings for Neon
- Added security and performance considerations

## Outcome

- ✅ Impact: Updated database schema specification with proper SQLModel code and migration steps
- 🧪 Tests: No tests created as this was a specification task
- 📁 Files: Updated specs/database/schema.md
- 🔁 Next prompts: Implementation of the database models based on this specification
- 🧠 Reflection: Successfully updated the schema with all required elements and proper indexing strategy

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of SQLModel classes based on this spec