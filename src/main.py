from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .users import create_user, get_user
from .tasks import create_task, get_tasks_for_user
from .repositories import task_repo

app = FastAPI(title="MCP Jira Git Demo")

class CreateUserIn(BaseModel):
    name: str
    email: str

class CreateTaskIn(BaseModel):
    title: str
    user_id: int

class TaskStatusUpdate(BaseModel):
    to_status: str

@app.post("/users")
def api_create_user(payload: CreateUserIn):
    u = create_user(payload.name, payload.email)
    return {"id": u.id, "name": u.name, "email": u.email}

@app.get("/users/{user_id}")
def api_get_user(user_id: int):
    u = get_user(user_id)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": u.id, "name": u.name, "email": u.email}

@app.post("/tasks")
def api_create_task(payload: CreateTaskIn):
    # missing: check that user exists (great Jira task)
    t = create_task(payload.title, payload.user_id)
    return {"id": t.id, "title": t.title, "user_id": t.user_id, "status": t.status}

@app.get("/users/{user_id}/tasks")
def api_get_tasks(user_id: int):
    items = get_tasks_for_user(user_id)
    return [{"id": t.id, "title": t.title, "user_id": t.user_id, "status": t.status} for t in items]

@app.post("/tasks/{task_id}/transition")
def api_transition_task(task_id: int, payload: TaskStatusUpdate):
    # Validate status
    valid_statuses = {"To Do", "In Progress", "Done"}
    if payload.to_status not in valid_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
        )
    
    # Check task exists
    task = task_repo.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update status
    updated_task = task_repo.transition(task_id, payload.to_status)
    return {"id": updated_task.id, "title": updated_task.title, "user_id": updated_task.user_id, "status": updated_task.status}
