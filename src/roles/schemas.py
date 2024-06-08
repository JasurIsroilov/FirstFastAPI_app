from pydantic import BaseModel

from .models import RolesEnum


class RolesDTO(BaseModel):
    name: RolesEnum

    class Config:
        from_attributes = True
        use_enum_values = True


class RolesReadDTO(RolesDTO):
    id: int
