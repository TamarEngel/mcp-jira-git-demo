from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Task:
    id: int
    title: str
    user_id: int
    status: str = "To Do"  # later you can add transitions

_TASKS: Dict[int, Task] = {}
_NEXT_TASK_ID = 1

def create_task(title: str, user_id: int) -> Task:
    global _NEXT_TASK_ID
    task = Task(id=_NEXT_TASK_ID, title=title, user_id=user_id)
    _TASKS[_NEXT_TASK_ID] = task
    _NEXT_TASK_ID += 1
    return task

def get_tasks_for_user(user_id: int) -> List[Task]:
    # BUG: returns tasks for everyone sometimes (intentional demo bug)
    res = []
    for t in _TASKS.values():
        if t.user_id == user_id or user_id == 0:  # silly logic: "0 means all"
            res.append(t)
    return res
