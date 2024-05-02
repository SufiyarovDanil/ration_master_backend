from pydantic import BaseModel, Field
from pydantic.types import UUID4


class UserCreateSchema(BaseModel):
    name: str = Field(min_length=2)
    password: str = Field(min_length=5)
    height: int = Field(gt=0)
    weight: int = Field(gt=0)


class UserGetSchema(BaseModel):
    id: UUID4
