"""Repository classes for data storage - replacing global dicts"""
from dataclasses import dataclass
from typing import Dict, Optional, List


@dataclass
class User:
    id: int
    name: str
    email: str


@dataclass
class Task:
    id: int
    title: str
    user_id: int
    status: str = "To Do"


class UserRepository:
    """Repository for managing users"""
    
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._next_id = 1
    
    def create(self, name: str, email: str) -> User:
        """Create a new user"""
        user = User(id=self._next_id, name=name, email=email)
        self._users[self._next_id] = user
        self._next_id += 1
        return user
    
    def get(self, user_id: int) -> Optional[User]:
        """Get a user by id"""
        return self._users.get(user_id)
    
    def get_all(self) -> List[User]:
        """Get all users"""
        return list(self._users.values())


class TaskRepository:
    """Repository for managing tasks"""
    
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_task_id = 1
    
    def create(self, title: str, user_id: int) -> Task:
        """Create a new task"""
        task = Task(id=self._next_task_id, title=title, user_id=user_id)
        self._tasks[self._next_task_id] = task
        self._next_task_id += 1
        return task
    
    def get(self, task_id: int) -> Optional[Task]:
        """Get a task by id"""
        return self._tasks.get(task_id)
    
    def get_by_user(self, user_id: int) -> List[Task]:
        """Get all tasks for a specific user"""
        return [t for t in self._tasks.values() if t.user_id == user_id]
    
    def get_all(self) -> List[Task]:
        """Get all tasks"""
        return list(self._tasks.values())
    
    def delete(self, task_id: int) -> bool:
        """Delete a task. Returns True if deleted, False if not found."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
    
    def transition(self, task_id: int, to_status: str) -> Optional[Task]:
        """Change task status. Returns updated task or None if not found."""
        if task_id not in self._tasks:
            return None
        self._tasks[task_id].status = to_status
        return self._tasks[task_id]


# Global repository instances
user_repo = UserRepository()
task_repo = TaskRepository()
