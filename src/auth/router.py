from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .schemas import RegisterSchema

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(new_user: RegisterSchema, session: AsyncSession = Depends(get_async_session)):

    return {"msg": "Success"}
