from api.schemas.calculation import GenderEnum, PhysicalActivityEnum


def __calc_bmr(weight: int, height: int, age: int, gender: GenderEnum) -> float:
    """
    Вычисление базового метаболизма
    """
    if gender == GenderEnum.male:
        return 655.0 + 9.6 * weight + 1.8 * height - 4.7 * age
    
    return 66.0 + 13.7 * weight + 5.0 * height - 6.8 * age


def __get_activity_coefficient(physical_activity: PhysicalActivityEnum) -> float:
    match physical_activity:
        case PhysicalActivityEnum.weight_gain:
            return 1.9
        case PhysicalActivityEnum.weight_keep:
            return 1.55
        case PhysicalActivityEnum.weight_loss:
            return 1.2


def calc_cpfc(age: int, weight: int, height: int, gender: GenderEnum,
         physical_activity: PhysicalActivityEnum) -> dict[str, int]:
    """
    Вычисление калорий и БЖУ
    """

    bmr: float = __calc_bmr(weight, height, age, gender)
    ac: float = __get_activity_coefficient(physical_activity)
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

    return {
        "calorie": int(calorie),
        "protein": int(protein),
        "fat": int(fat),
        "carbohydrate": int(carbohydrate)
    }
