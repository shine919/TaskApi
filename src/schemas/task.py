from pydantic import BaseModel


class Task(BaseModel):
    id:int
    task_name:str
    task_text:str
    user_id:int
    group_id:int


class CreateTask(Task):
    pass
