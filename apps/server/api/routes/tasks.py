from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from sqlmodel import Session, select, func
from models.task import Task, TaskCreate, TaskRead, TaskUpdate
from auth.jwt import get_current_user, TokenData
from database.session import get_db

# Create the API router
router = APIRouter()

@router.get("/", response_model=List[TaskRead])
async def list_tasks(
    current_user: TokenData = Depends(get_current_user),
    status: Optional[str] = Query(None, description="Filter by completion status: all, pending, completed"),
    sort: Optional[str] = Query("-created_at", description="Sort by field: created_at, -created_at, title, -title"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Get all tasks for the authenticated user with filtering, sorting, and pagination.
    """
    # Build the query
    query = select(Task).where(Task.user_id == current_user.user_id)

    # Apply status filter
    if status and status != "all":
        if status == "pending":
            query = query.where(Task.completed == False)
        elif status == "completed":
            query = query.where(Task.completed == True)

    # Apply sorting
    if sort:
        if sort == "created_at":
            query = query.order_by(Task.created_at)
        elif sort == "-created_at":
            query = query.order_by(Task.created_at.desc())
        elif sort == "title":
            query = query.order_by(Task.title)
        elif sort == "-title":
            query = query.order_by(Task.title.desc())

    # Apply pagination
    offset = (page - 1) * limit
    query = query.offset(offset).limit(limit)

    tasks = db.exec(query).all()
    return tasks

@router.post("/", response_model=TaskRead, status_code=201)
async def create_task(
    task: TaskCreate,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new task for the authenticated user.
    """
    db_task = Task(
        **task.dict(),
        user_id=current_user.user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    task_id: int,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a specific task by ID for the authenticated user.
    """
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Check ownership
    if task.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this task")

    return task

@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update a specific task for the authenticated user.
    """
    db_task = db.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Check ownership
    if db_task.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    # Update the task with provided values
    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete a specific task for the authenticated user.
    """
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Check ownership
    if task.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

@router.patch("/{task_id}/complete", response_model=TaskRead)
async def toggle_task_completion(
    task_id: int,
    completed: bool,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Toggle the completion status of a task for the authenticated user.
    """
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Check ownership
    if task.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    task.completed = completed
    db.add(task)
    db.commit()
    db.refresh(task)
    return task