from enum import Enum

from pydantic import BaseModel, Field
from pydantic.types import UUID4, FutureDatetime


class MealTime(Enum):
    breakfast = 'breakfast'
    dinner = 'dinner'
    supper = 'supper'


class RationCreateSchema(BaseModel):
    product_id: UUID4
    meal_time: MealTime = Field(default=MealTime.breakfast)
    product_gramm: int = Field(gt=0)
    time_to_eat: FutureDatetime


class RationGetSchema(BaseModel):
    id: UUID4
