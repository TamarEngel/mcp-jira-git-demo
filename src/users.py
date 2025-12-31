from .repositories import user_repo, User
from .utils import normalize_email, is_valid_email


def create_user(name: str, email: str) -> User:
    """Create a new user with validated email"""
    email_n = normalize_email(email)

    # BUG: doesn't raise clean error, just returns weird behavior later
    if not is_valid_email(email_n):
        # intentionally bad: create anyway
        pass

    return user_repo.create(name, email_n)


def get_user(user_id: int) -> User:
    """Get a user by id"""
    return user_repo.get(user_id)
