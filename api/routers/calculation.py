from fastapi import APIRouter

from api.schemas import OutputSchema
from api.schemas.calculation import GenderEnum, PhysicalActivityEnum


router: APIRouter = APIRouter(
    prefix='/api',
    tags=['calculation']
)


def calc_bmr(weight: int, height: int, age: int, gender: GenderEnum) -> float:
    """
    Вычисление базового метаболизма
    """
    if gender == GenderEnum.male:
        return 88.36 + 13.4 * weight + 4.8 * height - 5.7 * age
    
    return 447.6 + 9.2 * weight + 3.1 * height - 4.3 * age


def get_activity_coefficient(physical_activity: PhysicalActivityEnum) -> float:
    match physical_activity:
        case PhysicalActivityEnum.weight_gain:
            return 1.9
        case PhysicalActivityEnum.weight_keep:
            return 1.55
        case PhysicalActivityEnum.weight_loss:
            return 1.2


@router.get('/calculate_cpfc/{age}/{weight}/{height}/{gender}/{physical_activity}')
async def calculate_cpfc(
    age: int, weight: int, height: int, gender: GenderEnum,
    physical_activity: PhysicalActivityEnum) -> OutputSchema:
    """
    Вычисление калорий и БЖУ
    """

    bmr: float = calc_bmr(weight, height, age, gender)
    ac: float = get_activity_coefficient(physical_activity)
    calorie: float = bmr * ac

    if physical_activity == PhysicalActivityEnum.weight_loss:
        calorie -= 750.0
    if physical_activity == PhysicalActivityEnum.weight_gain:
        calorie += 400.0

    result = OutputSchema()

    result.data = {"calorie": calorie}

    return result
