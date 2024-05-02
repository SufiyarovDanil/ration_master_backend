from fastapi import APIRouter
from pydantic.types import UUID4

from api.schemas import OutputSchema
from api.schemas.ration import RationCreateSchema
from src import ration as ration_service

router: APIRouter = APIRouter(
    prefix='/api',
    tags=['Ration']
)


@router.post('/rations/create')
async def create_ration(ration_schema: RationCreateSchema) -> OutputSchema:
    ration_id = ration_service.create_ration(
        ration_schema.user_id,
        ration_schema.product_id,
        ration_schema.product_gramm,
        ration_schema.time_to_eat
    )
    result = OutputSchema()

    if ration_id:
        result.data = ration_id
    else:
        result.error = "Failed to create ration!"

    return result


@router.delete('/rations/{ration_id}')
async def remove_ration(ration_id: UUID4) -> OutputSchema:
    deleted = ration_service.remove_ration(ration_id)
    result = OutputSchema()

    if not deleted:
        result.error = "Ration not found!"

    return result


@router.get('/rations')
async def get_all_rations() -> OutputSchema:
    rations = ration_service.get_all_rations()
    result = OutputSchema()

    if rations:
        result.data = { "rations": [{"id": ration.id,
                                     "user_id": ration.user_id,
                                     "product": {
                                         "id": ration.product.id,
                                         "name": ration.product.name,
                                         "protein": ration.product.protein,
                                         "fat": ration.product.fat,
                                         "carbohydrate": ration.product.carbohydrate
                                     },
                                     "product_gramm": ration.product_gramm,
                                     "time_to_eat": ration.time_to_eat} for ration in rations]}
    else:
        result.error = "Rations not found!"

    return result


@router.get('/rations/{ration_id}')
async def get_ration(ration_id: UUID4) -> OutputSchema:
    ration = ration_service.get_ration(ration_id)
    result = OutputSchema()

    if ration:
        result.data = {
            "user_id": ration.user_id,
            "product": {
                "id": ration.product.id,
                "name": ration.product.name,
                "protein": ration.product.protein,
                "fat": ration.product.fat,
                "carbohydrate": ration.product.carbohydrate
            },
            "product_gramm": ration.product_gramm,
            "time_to_eat": ration.time_to_eat
        }
    else:
        result.error = "Ration not found!"

    return result
