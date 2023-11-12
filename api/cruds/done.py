from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model


async def get_done(db: AsyncSession, task_id: int) -> task_model.Done | None:
    result: Result = await db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    return result.scalars().first()


async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
    # DBモデルであるtask_model.Doneに変換する
    done = task_model.Done(id=task_id)
    db.add(done)
    await db.commit()
    # DB上のデータを元にTaskインスタンスであるdoneを更新する（この場合、作成したレコードのidを取得する）
    await db.refresh(done)
    return done


async def delete_done(db: AsyncSession, original: task_model.Done) -> task_model.Done.id:
    await db.delete(original)
    await db.commit()

    return original.id
