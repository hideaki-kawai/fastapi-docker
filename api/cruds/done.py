from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model


def get_done(db: Session, task_id: int) -> task_model.Done | None:
    result: Result = db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    return result.scalars().first()


def create_done(db: Session, task_id: int) -> task_model.Done:
    # DBモデルであるtask_model.Doneに変換する
    done = task_model.Done(id=task_id)
    db.add(done)
    db.commit()
    db.refresh(done)  # DB上のデータを元にTaskインスタンスであるdoneを更新する（この場合、作成したレコードのidを取得する）
    return done


def delete_done(db: Session, original: task_model.Done) -> task_model.Done.id:
    db.delete(original)
    db.commit()

    return original.id
