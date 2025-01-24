import asyncio
from datetime import datetime, timezone
from typing import Type

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import session_factory
from src.models import Group
from src.group.group_schema import GroupCreate, GroupUpdate, GroupUpdatePatch


async def create_group(session: AsyncSession, group_in: GroupCreate) -> Group:
    group = Group(**group_in.model_dump())
    session.add(group)
    await session.commit()
    await session.refresh(group)
    return group


async def update_group(
    session: AsyncSession,
    group: Group,
    group_update: GroupUpdate | GroupUpdatePatch,
    partial: bool = False,
) -> Group:
    for key, value in group_update.model_dump(exclude_unset=partial).items():
        setattr(group, key, value)
    group.updated_at = datetime.now(timezone.utc)
    await session.commit()
    return group
