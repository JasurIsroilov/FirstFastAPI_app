from typing import Annotated

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import BaseOrm


_idx_str_100 = Annotated[str, mapped_column(String(100))]


class UsersOrm(BaseOrm):

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[_idx_str_100] = mapped_column(unique=True)
    username: Mapped[_idx_str_100] = mapped_column(unique=True)
    phone_number: Mapped[_idx_str_100] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))

    role: Mapped["RolesOrm"] = relationship(back_populates="users")
