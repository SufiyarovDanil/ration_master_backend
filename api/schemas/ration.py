from pydantic import BaseModel, Field
from pydantic.types import UUID4, FutureDatetime


class RationCreateSchema(BaseModel):
    user_id: UUID4
    product_id: UUID4
    product_gramm: int = Field(gt=0)
    time_to_eat: FutureDatetime


class RationGetSchema(BaseModel):
    id: UUID4
