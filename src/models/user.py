from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from src.models.group import Group
    from src.models.task import Task


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    user_email: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    salt: Mapped[str] = mapped_column(String, nullable=False)
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="users")
    groups: Mapped[list["Group"]] = relationship(
        "Group", secondary="group_user_association", back_populates="users"
    )
