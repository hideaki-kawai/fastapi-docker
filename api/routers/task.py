import logging
from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のToDoタスク", done=False)]


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskRequest):
    try:
        result = task_schema.TaskCreateResponse(id=1, **task_body.dict())
        return result
    except Exception as e:
        logging.error(f"Error creating task: {str(e)}")
        raise


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskRequest):
    try:
        result = task_schema.TaskCreateResponse(id=task_id, **task_body.dict())
        return result
    except Exception as e:
        logging.error(f"Error creating task: {str(e)}")
        raise


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    pass


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
    pass


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int):
    pass
