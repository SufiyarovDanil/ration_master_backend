from fastapi import APIRouter
from pydantic.types import UUID4

from api.schemas import OutputSchema
from api.schemas.product import ProductCreateSchema
from src import product as prod_service


router: APIRouter = APIRouter(
    prefix='/api',
    tags=['Product']
)


@router.post('/products/create')
async def create_product(prod_schema: ProductCreateSchema) -> OutputSchema:
    prod_id = prod_service.create_product(
        prod_schema.name,
        prod_schema.calorie,
        prod_schema.protein,
        prod_schema.fat,
        prod_schema.carbohydrate
    )
    result = OutputSchema()

    if prod_id:
        result.data = prod_id
    else:
        result.error = "Failed to create product!"

    return result


@router.delete('/products/{prod_id}')
async def remove_user(prod_id: UUID4) -> OutputSchema:
    deleted = prod_service.remove_product(prod_id)
    result = OutputSchema()

    if not deleted:
        result.error = "Product not found!"

    return result


@router.get('/products')
async def get_all_products() -> OutputSchema:
    prods = prod_service.get_all_products()
    result = OutputSchema()

    if prods:
        result.data = {"products": [{"id": prod.id,
                                     "name": prod.name,
                                     "protein": prod.protein,
                                     "fat": prod.fat,
                                     "carbohydrate": prod.carbohydrate} for prod in prods]}
    else:
        result.error = "Products not found!"

    return result


@router.get('/products/{prod_id}')
async def get_user(prod_id: UUID4) -> OutputSchema:
    prod = prod_service.get_product(prod_id)
    result = OutputSchema()

    if prod:
        result.data = {
            "name": prod.name,
            "protein": prod.protein,
            "fat": prod.fat,
            "carbohydrate": prod.carbohydrate
        }
    else:
        result.error = "Product not found!"

    return result
