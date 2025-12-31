# MCP Jira Git Demo

A FastAPI application demonstrating a user and task management system with email validation.

## Features

- ✅ User management with email validation
- ✅ Task management with user association
- ✅ Email validation to prevent invalid emails
- ✅ Task filtering by user
- ✅ Delete operations for tasks
- ✅ Repository pattern for data storage

## Prerequisites

- Python 3.11+
- pip (Python package manager)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/TamarEngel/mcp-jira-git-demo.git
cd mcp-jira-git-demo
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

#### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Users

#### Create User
```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

**Response (201):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Error Response (400) - Invalid Email:**
```json
{
  "detail": "Invalid email: john@invalid"
}
```

#### Get User
```bash
curl -X GET "http://localhost:8000/users/1"
```

**Response (200):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Error Response (404):**
```json
{
  "detail": "User not found"
}
```

### Tasks

#### Create Task
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "user_id": 1
  }'
```

**Response (200):**
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "user_id": 1,
  "status": "To Do"
}
```

**Error Response (404) - User Not Found:**
```json
{
  "detail": "User not found"
}
```

#### Get Tasks for User
```bash
curl -X GET "http://localhost:8000/users/1/tasks"
```

**Response (200):**
```json
[
  {
    "id": 1,
    "title": "Complete project documentation",
    "user_id": 1,
    "status": "To Do"
  },
  {
    "id": 2,
    "title": "Review code",
    "user_id": 1,
    "status": "To Do"
  }
]
```

#### Delete Task
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

**Response (200):**
```json
{
  "deleted": true,
  "id": 1
}
```

**Error Response (404):**
```json
{
  "detail": "Task not found"
}
```

## Validation Rules

### Email Validation
- Email must be in valid format (contain @ symbol)
- Email cannot be empty
- Both user creation and task creation validate that the user exists

### Examples

**Valid Emails:**
```
user@example.com
john.doe@company.co.uk
test+tag@domain.org
```

**Invalid Emails:**
```
invalid.email
user@
@domain.com
not-an-email
```

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

Expected output:
```
tests/test_users.py::test_create_user_normalizes_email PASSED
tests/test_users.py::test_create_user_rejects_invalid_email FAILED (expected)
```

The failing test demonstrates the email validation requirement.

## Project Structure

```
mcp-jira-git-demo/
├── src/
│   ├── main.py          # FastAPI application
│   ├── users.py         # User logic with email validation
│   ├── tasks.py         # Task logic
│   ├── repositories.py   # Data storage repositories
│   ├── utils.py         # Utility functions (email validation)
│   └── __init__.py
├── tests/
│   ├── test_users.py    # User tests
│   └── __init__.py
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Invalid request (e.g., invalid email) |
| 404 | Resource not found (user or task) |

## Development

### Adding New Features

1. Create a feature branch: `git checkout -b feature/kan-XX`
2. Make your changes
3. Test thoroughly
4. Create a pull request with a clear description

### Code Style

- Follow PEP 8 guidelines
- Use type hints for function parameters and returns
- Write descriptive docstrings

## License

This project is part of the MCP Jira Git Demo.

## Contributing

For issues and feature requests, please use the Jira board.
