from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from .users import create_user, get_user
from .tasks import create_task, get_tasks_for_user, delete_task

app = FastAPI(title="MCP Jira Git Demo")

class CreateUserIn(BaseModel):
    name: str
    email: str
    
    @field_validator('email')
    @classmethod
    def validate_email_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Email cannot be empty")
        return v

class CreateTaskIn(BaseModel):
    title: str
    user_id: int

@app.post("/users")
def api_create_user(payload: CreateUserIn):
    try:
        u = create_user(payload.name, payload.email)
        return {"id": u.id, "name": u.name, "email": u.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/{user_id}")
def api_get_user(user_id: int):
    u = get_user(user_id)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": u.id, "name": u.name, "email": u.email}

@app.post("/tasks")
def api_create_task(payload: CreateTaskIn):
    # Check that user exists before creating task
    user = get_user(payload.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    t = create_task(payload.title, payload.user_id)
    return {"id": t.id, "title": t.title, "user_id": t.user_id, "status": t.status}

@app.get("/users/{user_id}/tasks")
def api_get_tasks(user_id: int):
    items = get_tasks_for_user(user_id)
    return [{"id": t.id, "title": t.title, "user_id": t.user_id, "status": t.status} for t in items]

@app.delete("/tasks/{task_id}")
def api_delete_task(task_id: int):
    if delete_task(task_id):
        return {"deleted": True, "id": task_id}
    else:
        raise HTTPException(status_code=404, detail="Task not found")
