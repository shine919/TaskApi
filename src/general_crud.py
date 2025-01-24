from datetime import timezone, datetime

from fastapi import Path, HTTPException, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Annotated, Union

from src.group.group_schema import GroupCreate, GroupUpdatePatch, GroupUpdate
from src.task.task_schema import TaskCreate, TaskUpdate, TaskUpdatePatch

T = TypeVar('T')


async def get_objects(session: AsyncSession, model: T) -> list[T]:
    stmt = select(model).order_by(model.id)
    result: Result = await session.execute(stmt)
    objects = result.scalars().all()
    return list(objects)


async def object_by_id(
    object_id: Annotated[int, Path],
    model: T,
    session: AsyncSession,
) -> T:
    object = await session.get(model, object_id)
    if object is not None:
        return object
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Group {object_id} not found"
    )


async def delete_obj(
    session: AsyncSession,
    model: T,
    object_id: Annotated[int, Path],
) -> None:
    obj = await object_by_id(object_id, model, session)
    await session.delete(obj)
    await session.commit()


async def create_obj(
    session: AsyncSession, obj: Union[GroupCreate, TaskCreate], model: T
) -> T:
    stmt = model(**obj.model_dump())
    session.add(stmt)
    await session.commit()
    await session.refresh(stmt)
    return stmt


async def update_obj(
    session: AsyncSession,
    model: T,
    object_id: Annotated[int, Path],
    obj_update: Union[GroupUpdate | GroupUpdatePatch | TaskUpdate | TaskUpdatePatch],
    partial: bool = False,
) -> T:
    obj = await object_by_id(object_id, model, session)
    for key, value in obj_update.model_dump(exclude_unset=partial).items():
        setattr(obj, key, value)
    obj.updated_at = datetime.now(timezone.utc)
    await session.commit()
    return obj
