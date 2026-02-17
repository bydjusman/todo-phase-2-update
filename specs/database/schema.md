# Database Schema Specification

## Overview

This document specifies the database schema for the Todo Web App, including the structure of the tasks table and other related entities. The schema is designed to work with SQLModel and integrate with Better Auth's user system.

## Tasks Table

### Requirements
- user_id: string, foreign key to Better Auth users.id
- title: string, not null, max 200
- description: text, nullable
- completed: bool, default false
- created_at, updated_at timestamps
- Indexes for fast filtering by user & status

### SQLModel Definition

```python
from sqlmodel import SQLModel, Field, create_engine
from typing import Optional
from sqlalchemy import Column, DateTime, Index, Text
from datetime import datetime

class Task(SQLModel, table=True):
    """
    Task model representing a user's todo item.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(
        ...,
        max_length=255,
        description="Foreign key to Better Auth users.id",
        index=True
    )
    title: str = Field(
        ...,
        max_length=200,
        description="Task title (max 200 chars)",
        nullable=False
    )
    description: Optional[str] = Field(
        default=None,
        description="Task description"
    )
    completed: bool = Field(
        default=False,
        description="Task completion status"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Task creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Task last update timestamp"
    )

    # Indexes for fast filtering
    __table_args__ = (
        # Index for filtering by user
        Index("idx_task_user_id", "user_id"),
        # Index for filtering by completion status
        Index("idx_task_completed", "completed"),
        # Combined index for filtering by user and status
        Index("idx_task_user_completed", "user_id", "completed"),
    )
```

### Field Specifications

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | int | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each task |
| user_id | string | NOT NULL, MAX(255), Foreign Key, Indexed | Links to Better Auth user ID |
| title | string | NOT NULL, MAX(200) | Task title with character limit |
| description | text | NULLABLE | Optional detailed task description |
| completed | boolean | DEFAULT false | Task completion status |
| created_at | datetime | NOT NULL, DEFAULT now | Timestamp of creation |
| updated_at | datetime | NOT NULL, DEFAULT now, ON UPDATE now | Timestamp of last update |

### Indexes

| Index Name | Fields | Purpose |
|------------|--------|---------|
| idx_task_user_id | user_id | Fast lookup of tasks by user |
| idx_task_completed | completed | Fast lookup of completed/incomplete tasks |
| idx_task_user_completed | user_id, completed | Fast lookup of user's completed/incomplete tasks |

## Additional Tables (Future Considerations)

### Users Table (Reference)

Better Auth manages the users table, but we'll reference its structure for our foreign key relationships:

```python
class UserLink(SQLModel):
    """
    This is a reference model showing the Better Auth user structure
    that our tasks table references.
    """
    id: str = Field(..., max_length=255)  # Better Auth user ID
    email: str = Field(..., max_length=255)
    created_at: datetime
    updated_at: datetime
```

## Migration Considerations

### Initial Database Setup

1. Create the tasks table
2. Set up required indexes
3. Configure foreign key relationships to Better Auth users

### Suggested Migration Steps

1. **Create Tasks Table**:
   ```sql
   CREATE TABLE tasks (
     id SERIAL PRIMARY KEY,
     user_id VARCHAR(255) NOT NULL,
     title VARCHAR(200) NOT NULL,
     description TEXT,
     completed BOOLEAN DEFAULT FALSE,
     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
     updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
   );
   ```

2. **Add Indexes**:
   ```sql
   CREATE INDEX idx_task_user_id ON tasks(user_id);
   CREATE INDEX idx_task_completed ON tasks(completed);
   CREATE INDEX idx_task_user_completed ON tasks(user_id, completed);
   ```

3. **Configure Foreign Key** (if Better Auth uses a compatible schema):
   ```sql
   ALTER TABLE tasks ADD CONSTRAINT fk_tasks_user_id
   FOREIGN KEY (user_id) REFERENCES auth_user(id);
   ```

### Migration Considerations for Better Auth Integration

- Better Auth may use a different table structure for users
- The foreign key relationship may need to be adjusted based on Better Auth's actual implementation
- Consider using a UUID for user_id if Better Auth uses UUIDs
- Verify the actual column name used by Better Auth for user identification

## Database Connection Settings

### Neon Configuration

```python
DATABASE_URL = "postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname"

# Connection pool settings
POOL_SIZE = 10
MAX_OVERFLOW = 20
POOL_TIMEOUT = 30
POOL_RECYCLE = 3600
```

## Security Considerations

- User data is isolated by user_id foreign key
- Completed status allows for privacy controls
- Timestamps provide audit trail
- Indexes should not expose sensitive information

## Performance Optimization

- Indexes on user_id enable fast user-specific queries
- Indexes on completed status enable fast status filtering
- Combined index optimizes common user + status queries
- Consider partitioning for very large datasets</content>
<parameter name="filePath">d:\todo-app\todo-app-phase-2\specs\database\schema.md