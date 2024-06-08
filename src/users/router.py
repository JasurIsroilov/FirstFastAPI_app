from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .schemas import UsersAddDTO, UsersReadDTO, UsersActionDTO
from .utils import (
    db_register_user,
    db_activate_user,
    db_deactivate_user,
    db_verify_user,
    db_delete_user,
    db_get_user_by_id,
)


router = APIRouter(prefix="/users", tags=["User"])


@router.get("/{user_id}")
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)) -> UsersReadDTO | None:
    user = await db_get_user_by_id(user_id, session)
    return user


@router.post("/create")
async def create(new_user: UsersAddDTO, session: AsyncSession = Depends(get_async_session)):
    new_user_dict = new_user.dict()
    await db_register_user(new_user_dict, session)
    return {"msg": "Success"}


@router.post("/activate")
async def activate(user: UsersActionDTO, session: AsyncSession = Depends(get_async_session)):
    await db_activate_user(user.id, session)
    return {"msg": "User activated!"}


@router.post("/deactivate")
async def deactivate(user: UsersActionDTO, session: AsyncSession = Depends(get_async_session)):
    await db_deactivate_user(user.id, session)
    return {"msg": "User deactivated!"}


@router.post("/verify")
async def verify(user: UsersActionDTO, session: AsyncSession = Depends(get_async_session)):
    await db_verify_user(user.id, session)
    return {"msg": "User verified!"}


@router.delete("/{user_id}")
async def delete(user_id: int, session: AsyncSession = Depends(get_async_session)):
    await db_delete_user(user_id, session)
    return {"msg": "User deleted!"}
