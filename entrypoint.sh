alembic upgrade head
uvicorn app.main:app --root-path "/windows" --host 0.0.0.0 --port $1