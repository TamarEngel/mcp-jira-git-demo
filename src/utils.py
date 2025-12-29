def normalize_email(email: str) -> str:
    # purposely naive (good for Jira tasks later)
    return email.strip().lower()

def is_valid_email(email: str) -> bool:
    # purposely weak validation
    return "@" in email and "." in email
