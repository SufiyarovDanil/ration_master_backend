import random as rnd

from fastapi import APIRouter

from api.schemas import OutputSchema
from api.schemas.calculation import GenderEnum, PhysicalActivityEnum
import src.calculation as calc_service
import src.product as prod_service


router: APIRouter = APIRouter(
    prefix='/api',
    tags=['calculation']
)


@router.get('/calculate_cpfc/{age}/{weight}/{height}/{gender}/{physical_activity}')
async def calculate_cpfc(
    age: int, weight: int, height: int, gender: GenderEnum,
    physical_activity: PhysicalActivityEnum) -> OutputSchema:
    """
    Вычисление калорий и БЖУ
    """

    cpfc = calc_service.calc_cpfc(age, weight, height, gender, physical_activity)
    result = OutputSchema()
    result.data = cpfc

    return result


@router.get('/calculate_ration/{age}/{weight}/{height}/{gender}/{physical_activity}')
async def calculate_ration(
    age: int, weight: int, height: int, gender: GenderEnum,
    physical_activity: PhysicalActivityEnum) -> OutputSchema:
    """

    """
    cpfc = calc_service.calc_cpfc(age, weight, height, gender,
                                  physical_activity)
    prods = prod_service.get_all_products()
    result = OutputSchema()

    if not prods:
        result.error = 'products not found!'
        return result

    calorie_per_meal = cpfc['calorie'] / 3.0
    fitted_products = [{
        'name': i.name,
        'calorie': int(calorie_per_meal),
        'protein': int(i.protein * (calorie_per_meal / i.calorie)),
        'fat': int(i.fat * (calorie_per_meal / i.calorie)),
        'carbohydrate': int(i.carbohydrate * (calorie_per_meal / i.calorie)),
        'gramms': int(100.0 * (calorie_per_meal / i.calorie))
    } for i in prods]
    ration = {
        'breakfast': None,
        'dinner': None,
        'supper': None
    }

    for meal in ration.keys():
        product = rnd.choice(fitted_products)
        ration[meal] = product
        fitted_products.remove(product)
    
    result.data = ration

    return result
