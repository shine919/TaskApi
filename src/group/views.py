from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src import general_crud
from src.general_crud import object_by_id, update_obj
from src.group import crud
from src.core.database import get_session
from src.models import Group as GroupModel
from src.group.group_schema import Group, GroupCreate, GroupUpdate, GroupUpdatePatch

router = APIRouter(tags=["Group"], prefix="/group")


@router.get("/", response_model=List[Group])
async def get_groups(
    session: AsyncSession = Depends(get_session),
):
    return await general_crud.get_objects(session, GroupModel)


@router.post("/", response_model=Group)
async def get_group(group_id: int, session: AsyncSession = Depends(get_session)):
    return await object_by_id(model=GroupModel, object_id=group_id, session=session)


@router.post("/{group_id}/", response_model=Group)
async def create_group(
    group_in: GroupCreate,
    session: AsyncSession = Depends(get_session),
):
    return await crud.create_group(session, group_in)


@router.put("/{group_id}/")
async def update_group(
    group_id: int,
    group_update: GroupUpdate,
    session: AsyncSession = Depends(get_session),
):
    group_obj = await object_by_id(
        model=GroupModel, object_id=group_id, session=session
    )
    updated_group = await crud.update_group(
        session=session,
        group=group_obj,
        group_update=group_update,
    )

    return None


@router.patch("/{group_id}/")
async def update_group(
    group_update: GroupUpdatePatch,
    group_id: int,
    session: AsyncSession = Depends(get_session),
):
    group_obj = await object_by_id(
        model=GroupModel,
        object_id=group_id,
        session=session,
    )
    updated_group = await crud.update_group(
        session=session,
        group=group_obj,
        group_update=group_update,
        partial=True,
    )
    return None


@router.delete("/{group_id}/")
async def delete_group(
    group_id: int,
    session: AsyncSession = Depends(get_session),
):
    await general_crud.delete_obj(session=session, model=GroupModel, object_id=group_id)
    return None
