from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(
        None, example="クリーニングを取りに行く")


class TaskRequest(TaskBase):
    pass


class TaskCreateResponse(TaskRequest):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True
