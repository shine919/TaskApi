import datetime
from typing import Annotated
from sqlalchemy.types import TIMESTAMP
from sqlalchemy import text, func, MetaData
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from src.core.config import settings

created_at = Annotated[
    datetime.datetime,
    mapped_column(TIMESTAMP(timezone=True), server_default=func.now()),
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    ),
]

intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=settings.dbconfig.convention)
    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
