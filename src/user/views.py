from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import general_crud
from src.general_crud import object_by_id, get_objects
from src.user import crud
from src.core.database import get_session
from src.models import User as UserModel
from src.user.user_schema import UserUpdatePatch, UserUpdate, UserCreate, User

router = APIRouter(tags=["User"], prefix="/user")


@router.get("/", response_model=List[User])
async def get_users(
    session: AsyncSession = Depends(get_session),
):
    return await get_objects(session, UserModel)


@router.post("/{user_id}/", response_model=User)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    user = await object_by_id(session=session, model=UserModel, object_id=user_id)
    return user


@router.post("/create/{user_id}/", response_model=User)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    return await crud.create_user(session=session, user_in=user_in)


@router.put("/update/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    user = await object_by_id(session=session, model=UserModel, object_id=user_id)
    return await crud.update_user(session=session, user=user, user_update=user_update)


@router.patch("/patch/{user_id}/")
async def update_user(
    user_update: UserUpdatePatch,
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    user = await object_by_id(session=session, model=UserModel, object_id=user_id)
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True,
    )


@router.delete("/delete/{user_id}/")
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
) -> str:
    await general_crud.delete_obj(session=session, model=UserModel, object_id=user_id)
    return 'Success delete user'
