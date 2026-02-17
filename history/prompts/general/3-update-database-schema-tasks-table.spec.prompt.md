---
id: 3
title: Update Database Schema with Tasks Table
stage: spec
date: 2026-02-16
surface: agent
model: Grok
feature: none
branch: main
user: user
command: 
labels: ["database", "schema", "sqlmodel"]
links:
  spec: 
  ticket: 
  adr: 
  pr: 
files:
 - specs/database/schema.md
tests:
---

## Prompt

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

## Response snapshot

Updated /specs/database/schema.md with comprehensive tasks table specification including SQLModel code, table structure, indexes, and migration steps for the Todo Web App database schema.

## Outcome

- ✅ Impact: Defined complete database schema for tasks table with proper relationships and indexes
- 🧪 Tests: No tests added
- 📁 Files: Created specs/database/schema.md
- 🔁 Next prompts: Implement Task model in apps/server/models/task.py
- 🧠 Reflection: Successfully created database specification with SQLModel code and migration guidance

## Evaluation notes (flywheel)

- Failure modes observed: 
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): 
- Next experiment (smallest change to try): </content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\history\prompts\general\3-update-database-schema-tasks-table.spec.prompt.md