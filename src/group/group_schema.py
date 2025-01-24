from pydantic import BaseModel, ConfigDict


class GroupBase(BaseModel):
    name: str


class Group(GroupBase):
    id: int


class GroupCreate(GroupBase):
    model_config = ConfigDict(from_attributes=True)


class GroupUpdate(GroupCreate):
    pass


class GroupUpdatePatch(GroupCreate):
    name: str | None = None
