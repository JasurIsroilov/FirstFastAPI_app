from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import RolesOrm
from .schemas import RolesReadDTO


async def db_get_role_by_name(role_name: str, session: AsyncSession) -> RolesReadDTO | None:
    stmt = select(RolesOrm).where(RolesOrm.name == role_name)
    res = await session.execute(stmt)
    return res.scalar()
