import asyncio
from datetime import datetime, timezone
from typing import List

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

# from src.core.database import session_factory
from src.models import User
from src.user.dependencies import hash_password
from src.user.user_schema import UserCreate, UserUpdate, UserUpdatePatch


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    password, salt = hash_password(user_in.password)
    user = User(
        username=user_in.username,
        user_email=user_in.user_email,
        password=password,
        salt=salt,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    # print(user.id, user.username)
    return user


async def update_user(
    session: AsyncSession,
    user_update: UserUpdate | UserUpdatePatch,
    user: User,
    partial: bool = False,
) -> User:
    for key, value in user_update.model_dump(exclude_unset=partial).items():
        if key == 'password':
            password, salt = hash_password(value)
            setattr(user, 'password', password)
            setattr(user, 'salt', salt)
            continue
        setattr(user, key, value)
    user.updated_at = datetime.now(timezone.utc)
    await session.commit()
    return user
