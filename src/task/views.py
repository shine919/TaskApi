from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.general_crud import (
    object_by_id,
    update_obj,
    create_obj,
    get_objects,
    delete_obj,
)
from src.core.database import get_session
from src.models import Task as TaskModel
from src.task.task_schema import Task, TaskCreate, TaskUpdate, TaskUpdatePatch


router = APIRouter(tags=["Task"], prefix="/task")


@router.get("/", response_model=List[Task])
async def get_tasks(
    session: AsyncSession = Depends(get_session),
):
    return await get_objects(session, TaskModel)


@router.post("/", response_model=Task)
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)):
    return await object_by_id(model=TaskModel, object_id=task_id, session=session)


@router.post("/{task_id}/", response_model=Task)
async def create_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(get_session),
):
    return await create_obj(session=session, obj=task_in, model=TaskModel)


@router.put("/{task_id}/")
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    session: AsyncSession = Depends(get_session),
):
    await update_obj(
        session=session, model=TaskModel, object_id=task_id, obj_update=task_update
    )

    return None


@router.patch("/{task_id}/")
async def update_task(
    task_update: TaskUpdatePatch,
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    await update_obj(
        session=session,
        model=TaskModel,
        object_id=task_id,
        obj_update=task_update,
        partial=True,
    )
    return None


@router.delete("/{task_id}/")
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    await delete_obj(session=session, model=TaskModel, object_id=task_id)
    return None
