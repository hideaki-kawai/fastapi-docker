from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model
import api.schemas.task as task_schema


def create_task(db: Session, task_request: task_schema.TaskRequest) -> task_model.Task:
    # DBモデルであるtask_model.Taskに変換する
    task = task_model.Task(**task_request.dict())
    db.add(task)
    db.commit()
    db.refresh(task)  # DB上のデータを元にTaskインスタンスであるtaskを更新する（この場合、作成したレコードのidを取得する）
    return task


def get_task_with_done(db: Session) -> list[tuple[int, str, bool]]:
    result: Result = db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Done.id.isnot(None).label("done"),
        ).outerjoin(task_model.Done)
    )

    return result.all()


def get_task(db: Session, task_id: int) -> task_model.Task | None:
    result: Result = db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    return result.scalars().first()


def update_task(db: Session, task_request: task_schema.TaskRequest, original: task_model.Task) -> task_model.Task:
    original.title = task_request.title
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


def delete_task(db: Session, original: task_model.Task) -> task_model.Task.id:
    db.delete(original)
    db.commit()

    return original.id
