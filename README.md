# PJ 作成時コマンド

### 以下のコマンドはなぜかエラーになったから pyproject.toml はローカルで`poetry init`して手動で作成した。

```
docker compose run --entrypoint "poetry init --name app --dependency fastapi --dependency uvicorn[standard]" app

[tool.poetry] section not found in /src/pyproject.toml
```

# FastAPI install

```
docker compose run --entrypoint "poetry install --no-root" app
```

# DB Migration
```
docker compose exec -it app bash

# -mはモジュールのm
poetry run python -m api.migrate_db
```
