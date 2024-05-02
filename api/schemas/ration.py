from pydantic import BaseModel
from pydantic.types import UUID4, FutureDatetime


class UserCreateSchema(BaseModel):
    user_id: UUID4
    product_id: UUID4
    product_gramm: int
    time_to_eat: FutureDatetime


class UserGetSchema(BaseModel):
    id: UUID4
