from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema


async def create_task(db: AsyncSession, task_request: task_schema.TaskRequest) -> task_model.Task:
    # DBモデルであるtask_model.Taskに変換する
    task = task_model.Task(**task_request.dict())
    db.add(task)
    await db.commit()
    # DB上のデータを元にTaskインスタンスであるtaskを更新する（この場合、作成したレコードのidを取得する）
    await db.refresh(task)
    return task


async def get_task_with_done(db: AsyncSession) -> list[tuple[int, str, bool]]:
    result: Result = await db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Done.id.isnot(None).label("done"),
        ).outerjoin(task_model.Done)
    )

    return result.all()


async def get_task(db: AsyncSession, task_id: int) -> task_model.Task | None:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    return result.scalars().first()


async def update_task(db: AsyncSession, task_request: task_schema.TaskRequest, original: task_model.Task) -> task_model.Task:
    original.title = task_request.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_task(db: AsyncSession, original: task_model.Task) -> task_model.Task.id:
    await db.delete(original)
    await db.commit()

    return original.id
