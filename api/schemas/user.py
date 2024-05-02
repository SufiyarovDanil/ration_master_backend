from pydantic import BaseModel
from pydantic.types import UUID4


class UserCreateSchema(BaseModel):
    name: str
    password: str
    height: int
    weight: int


class UserGetSchema(BaseModel):
    id: UUID4
