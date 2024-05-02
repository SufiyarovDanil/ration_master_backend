from pydantic import BaseModel
from pydantic.types import UUID4


class ProductCreateSchema(BaseModel):
    name: str
    protein: int
    fat: int
    carbohydrate: int


class ProductGetSchema(BaseModel):
    id: UUID4
