from typing import List
from .repositories import task_repo, Task


def create_task(title: str, user_id: int) -> Task:
    """Create a new task"""
    return task_repo.create(title, user_id)


def get_tasks_for_user(user_id: int) -> List[Task]:
    """Get all tasks for a specific user (fixed: no longer returns all tasks when user_id=0)"""
    return task_repo.get_by_user(user_id)


def delete_task(task_id: int) -> bool:
    """Delete a task by id. Returns True if deleted, False if not found."""
    return task_repo.delete(task_id)
