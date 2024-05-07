from enum import Enum

from pydantic import BaseModel, Field
from pydantic.types import UUID4


class GenderEnum(Enum):
    male = 'male'
    female = 'female'


class PhysicalActivityEnum(Enum):
    weight_loss = 'weight_loss'
    weight_gain = 'weight_gain'
    weight_keep = 'weight_keep'


class CalculateCpfcSchema(BaseModel):
    age: int = Field(gt=0)
    weight: int = Field(gt=0)
    height: int = Field(gt=0)
    gender: GenderEnum = Field(default=GenderEnum.male)
    physical_activity: PhysicalActivityEnum = Field(
        default=PhysicalActivityEnum.weight_loss)
