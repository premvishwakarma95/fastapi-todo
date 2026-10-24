# fastapi-todo (Repo to learn - https://github.com/navinreddy20/fastapi-demo)

A todo API built while learning FastAPI.

## Setup

Run these from the project folder.

### 1. Create the virtual environment

```bash
python3 -m venv .venv
```

### 2. Activate it

```bash
source .venv/bin/activate
```

The prompt should show `(.venv)`. Run this again in every new terminal.

### 3. Install FastAPI

```bash
pip install --upgrade pip
pip install "fastapi[standard]"
```

The `standard` extra also installs Uvicorn and the `fastapi` CLI. A plain `pip install fastapi` does not.

### 4. Save the dependencies

```bash
pip freeze > requirements.txt
```

On another machine, restore them with `pip install -r requirements.txt`.

### 5. Ignore junk in git

```bash
printf ".venv/\n__pycache__/\n*.pyc\n.env\n" > .gitignore
```

### 6. Create the app file

```bash
cat > main.py <<'EOF'
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
EOF
```

### 7. Run the dev server

```bash
fastapi dev main.py
```

Or: `uvicorn main:app --reload`

To use a different port (the default is 8000):

```bash
fastapi dev main.py --port 8080
uvicorn main:app --reload --port 8080
```

To listen on all network interfaces, not just localhost, add `--host 0.0.0.0`.

### 8. Open it in the browser

- API: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Project layout (target)

```
fastapi-todo/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routers/
│       └── todos.py
├── tests/
├── requirements.txt
└── .gitignore
```

Run it with `fastapi dev app/main.py` once the code moves into `app/`.

## Learning roadmap

| Stage | Build | You learn |
|---|---|---|
| 1. Basics | In-memory todo CRUD | Path operations, path and query params, request bodies, auto docs at `/docs` |
| 2. Validation | Pydantic models | Request and response models, `Field` constraints, status codes, `HTTPException` |
| 3. Structure | Split into routers | `APIRouter`, project layout, dependency injection (`Depends`) |
| 4. Database | SQLite with SQLModel or SQLAlchemy | Sessions as dependencies, migrations (Alembic) |
| 5. Auth | Users, password hashing, JWT | OAuth2 password flow, security dependencies, per-user todos |
| 6. Async and background | Async endpoints, background tasks | `async def` vs `def`, `BackgroundTasks`, lifespan events |
| 7. Production | Tests, config, deployment | `TestClient`, pytest, settings via env vars, middleware and CORS, Docker, Uvicorn/Gunicorn |
| 8. Advanced | Extras | WebSockets, file uploads, custom exceptions, pagination, rate limiting |
