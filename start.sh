#!/bin/sh

# マイグレーションを実行
poetry run python -m api.migrate_db

# uvicornを起動
exec poetry run uvicorn api.main:app --host 0.0.0.0 --reload
