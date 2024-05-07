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
    
    tdee: float = 0.0

    if gender == GenderEnum.male:
        tdee = 655.0 + 9.6 * weight + 1.8 * height - 4.7 * age
    else:
        tdee = 66.0 + 13.7 * weight + 5.0 * height - 6.8 * age

    protein: float = weight * 1.9
    fat: float = (tdee * 0.275) / 9.0
    carbohydrate: float = (tdee - protein * 4.0 - fat * 9.0) / 4.0
    result = OutputSchema()

    result.data = {
        "calorie": calorie,
        "protein": protein,
        "fat": fat,
        "carbohydrate": carbohydrate
    }

    return result
