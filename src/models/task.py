from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
import enum

if TYPE_CHECKING:
    from src.models.group import Group
    from src.models.user import User


class TaskStatus(enum.Enum):
    completed = 'completed'
    not_completed = 'not_completed'


class Task(Base):
    __tablename__ = 'tasks'

    task_name: Mapped[str] = mapped_column(String, nullable=False)
    task_text: Mapped[str] = mapped_column(String, nullable=True)
    task_status: Mapped[TaskStatus] = mapped_column(
        SqlEnum(TaskStatus, name='task_status'),
        server_default='not_completed',
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('users.id', ondelete='CASCADE')
    )
    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('groups.id', ondelete='CASCADE')
    )
    users: Mapped["User"] = relationship(back_populates="tasks")
    groups: Mapped["Group"] = relationship(back_populates="tasks")
