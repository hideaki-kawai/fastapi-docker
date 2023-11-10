#!/bin/sh

# データベースが起動するまで待機
echo "Waiting for db to be ready..."
while ! nc -z db 3306; do
  sleep 0.1
done
echo "DB is ready!"

# マイグレーションを実行
poetry run python -m api.migrate_db

# uvicornを起動
exec poetry run uvicorn api.main:app --host 0.0.0.0 --reload
