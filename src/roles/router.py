from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .models import RolesOrm
from .schemas import RolesDTO, RolesReadDTO

from database import get_async_session


router = APIRouter(prefix="/roles", tags=["Role"])


@router.post("/add")
async def add_role(new_role: RolesDTO, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(RolesOrm).values(**new_role.dict())
    try:
        await session.execute(stmt)
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=422, detail="Current role already exists!")
    return {"msg": "Success"}


@router.get("/")
async def roles(session: AsyncSession = Depends(get_async_session)) -> List[RolesReadDTO] | None:
    stmt = select(RolesOrm)
    res = await session.execute(stmt)
    return res.scalars().all()
