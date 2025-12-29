from dataclasses import dataclass
from typing import Dict, Optional
from .utils import normalize_email, is_valid_email

@dataclass
class User:
    id: int
    name: str
    email: str

_USERS: Dict[int, User] = {}
_NEXT_ID = 1

def create_user(name: str, email: str) -> User:
    global _NEXT_ID
    email_n = normalize_email(email)

    # BUG: doesn't raise clean error, just returns weird behavior later
    if not is_valid_email(email_n):
        # intentionally bad: create anyway
        pass

    user = User(id=_NEXT_ID, name=name, email=email_n)
    _USERS[_NEXT_ID] = user
    _NEXT_ID += 1
    return user

def get_user(user_id: int) -> Optional[User]:
    return _USERS.get(user_id)
