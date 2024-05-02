from pydantic import BaseModel, Field
from pydantic.types import UUID4


class ProductCreateSchema(BaseModel):
    name: str
    protein: int = Field(gt=0)
    fat: int = Field(gt=0)
    carbohydrate: int = Field(gt=0)


class ProductGetSchema(BaseModel):
    id: UUID4
