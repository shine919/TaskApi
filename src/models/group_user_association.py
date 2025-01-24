from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class GroupUserAssociation(Base):
    __tablename__ = 'group_user_association'
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey('groups.id', ondelete='CASCADE'))
