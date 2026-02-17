---
id: 5
title: Write Clean Feature Specification for Task Management
stage: spec
date: 2026-02-16
surface: agent
model: Grok
feature: tasks
branch: main
user: user
command: 
labels: ["feature", "specification", "tasks", "crud"]
links:
  spec: 
  ticket: 
  adr: 
  pr: 
files:
 - specs/features/tasks.md
tests:
---

## Prompt

SKILL: Write Clean Feature Specification

You are an expert at writing precise, testable, developer-friendly specifications.

Follow this exact structure:

# Feature: [Feature Name]

## Purpose
One clear sentence what this feature achieves.

## User Stories
- As a [user type], I want [goal] so that [benefit]
- ...

## Acceptance Criteria
### [Sub-feature / Happy path]
- Given [context]
- When [action]
- Then [expected outcome]

### [Another scenario]
...

## Edge Cases & Constraints
- [condition] → [behavior / error]
- Maximum / minimum values
- Required fields
- Invalid inputs

## Business Rules
- Any important logic or restrictions

## Related Specs
- @specs/features/...
- @specs/api/...
- @specs/database/...

## Open Questions / Decisions Needed
- List any unclear points

Rules:
- Use concrete, measurable criteria
- Avoid vague words ("good", "nice", "proper")
- Think about security, performance, UX implications
- Write in present tense
- Keep language unambiguous

Now write the specification for: [tell what to write]

## Response snapshot

Created comprehensive feature specification for Task Management in /specs/features/tasks.md following the exact required structure with user stories, acceptance criteria, edge cases, and business rules.

## Outcome

- ✅ Impact: Defined complete, testable specification for task CRUD functionality
- 🧪 Tests: Acceptance criteria include Given/When/Then scenarios for all operations
- 📁 Files: Created specs/features/tasks.md
- 🔁 Next prompts: Implement the Task model and API endpoints
- 🧠 Reflection: Successfully created developer-friendly spec with clear constraints and security considerations

## Evaluation notes (flywheel)

- Failure modes observed: 
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): 
- Next experiment (smallest change to try): </content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\history\prompts\tasks\5-write-clean-feature-specification-task-management.spec.prompt.md