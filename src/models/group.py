from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from src.models.task import Task
    from src.models.user import User


class Group(Base):
    __tablename__ = 'groups'

    name: Mapped[str] = mapped_column(String, nullable=False)
    users: Mapped[list["User"]] = relationship(
        secondary="group_user_association", back_populates="groups"
    )
    tasks: Mapped[list["Task"]] = relationship(back_populates="groups")
