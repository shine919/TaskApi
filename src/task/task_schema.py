from pydantic import BaseModel, ConfigDict
import enum
from src.models.task import TaskStatus


class TaskBase(BaseModel):
    task_name: str
    task_text: str | None = None
    task_status: TaskStatus = TaskStatus.not_completed
    user_id: int
    group_id: int


class Task(TaskBase):
    id: int


class TaskCreate(TaskBase):
    model_config = ConfigDict(from_attributes=True)


class TaskUpdate(TaskCreate):
    pass


class TaskUpdatePatch(TaskCreate):
    task_name: str | None = None
    task_text: str | None = None
    task_status: TaskStatus
