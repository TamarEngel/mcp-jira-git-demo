from src.users import create_user

def test_create_user_normalizes_email():
    u = create_user("Tamar", "  TAMAR@Example.Com ")
    assert u.email == "tamar@example.com"

def test_create_user_rejects_invalid_email():
    # This test should FAIL currently (intentional), to generate a Jira bug
    u = create_user("Bad", "not-an-email")
    assert "@" in u.email
