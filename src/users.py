from .repositories import user_repo, User
from .utils import normalize_email, is_valid_email


def create_user(name: str, email: str) -> User:
    """Create a new user with validated email"""
    email_n = normalize_email(email)

    # Validate email and raise error if invalid
    if not is_valid_email(email_n):
        raise ValueError(f"Invalid email: {email}")

    return user_repo.create(name, email_n)


def get_user(user_id: int) -> User:
    """Get a user by id"""
    return user_repo.get(user_id)
