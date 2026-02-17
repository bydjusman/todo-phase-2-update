from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone
import os

class TaskBase(SQLModel):
    title: str = Field(
        min_length=1,
        max_length=200,
        description="Task title (max 200 chars)"
    )
    description: Optional[str] = Field(
        default=None,
        description="Task description"
    )
    completed: bool = Field(
        default=False,
        description="Task completion status"
    )

class Task(TaskBase, table=True):
    """
    Task model representing a user's todo item.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(
        max_length=255,
        description="Foreign key to Better Auth users.id",
        sa_column_kwargs={"index": True}
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Task creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Task last update timestamp"
    )

class TaskCreate(TaskBase):
    """Task creation schema"""
    title: str = Field(
        min_length=1,
        max_length=200,
        description="Task title (max 200 chars)"
    )

class TaskRead(TaskBase):
    """Task reading schema"""
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime

class TaskUpdate(SQLModel):
    """Task update schema"""
    title: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=200
    )
    description: Optional[str] = None
    completed: Optional[bool] = None