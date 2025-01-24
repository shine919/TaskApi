from pydantic import BaseModel

from src.schemas.task import Task
from src.schemas.user import User


class Group(BaseModel):
    id:int
    name:str
    users:list[User]
    tasks:list[Task]


class CreateGroup(Group):
    pass
