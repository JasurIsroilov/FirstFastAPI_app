import enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import BaseOrm


class RolesEnum(enum.Enum):
    admin = "admin"
    superuser = "superuser"
    user = "user"


class RolesOrm(BaseOrm):

    __tablename__ = "roles"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[RolesEnum] = mapped_column(String(50), unique=True)

    users: Mapped[list["UsersOrm"]] = relationship(back_populates="role")
