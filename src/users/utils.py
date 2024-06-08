from fastapi import HTTPException

from sqlalchemy import update, insert, delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .errors import UsersErrors
from .models import UsersOrm
from roles.utils import db_get_role_by_name
from auth.password_manager import PasswordManager
from auth.user_manager import UserManager


async def db_register_user(new_user_dict: dict, session: AsyncSession):
    UserManager.validate_email(new_user_dict.get("email"))

    role = await db_get_role_by_name(role_name=new_user_dict.get("role"), session=session)
    new_user_dict["password"] = PasswordManager.get_hashed_pwd(new_user_dict.get("password"))
    new_user_dict.pop("role")
    new_user_dict["role_id"] = role.id
    stmt = insert(UsersOrm).values(**new_user_dict)

    try:
        await session.execute(stmt)
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=422, detail=UsersErrors.not_unique)
    return


async def db_get_user_by_id(user_id: int, session: AsyncSession):
    stmt = select(UsersOrm).where(UsersOrm.id == user_id)
    res = await session.execute(stmt)
    return res.scalar()


async def db_activate_user(user_id: int, session: AsyncSession):
    stmt = update(UsersOrm).where(UsersOrm.id == user_id).values(is_active=True)
    await session.execute(stmt)
    await session.commit()
    return


async def db_deactivate_user(user_id: int, session: AsyncSession):
    stmt = update(UsersOrm).where(UsersOrm.id == user_id).values(is_active=False)
    await session.execute(stmt)
    await session.commit()
    return


async def db_verify_user(user_id: int, session: AsyncSession):
    stmt = update(UsersOrm).where(UsersOrm.id == user_id).values(is_verified=True)
    await session.execute(stmt)
    await session.commit()
    return


async def db_delete_user(user_id: int, session: AsyncSession):
    stmt = delete(UsersOrm).where(UsersOrm.id == user_id)
    await session.execute(stmt)
    await session.commit()
    return
