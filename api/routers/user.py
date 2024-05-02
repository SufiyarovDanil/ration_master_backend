from uuid import UUID

from fastapi import APIRouter
from pydantic.types import UUID4

from api.schemas import OutputSchema
from api.schemas.user import UserCreateSchema
from src import user as user_service

router: APIRouter = APIRouter(
    prefix='/api',
    tags=['Album']
)


@router.post('/users/create')
async def create_user(user_schema: UserCreateSchema) -> OutputSchema:
    user_id = user_service.create_user(
        user_schema.name,
        user_schema.password,
        user_schema.height,
        user_schema.weight
    )
    result = OutputSchema()

    if user_id:
        result.data = user_id
    else:
        result.error = "Failed to create user!"

    return result


@router.delete('/users/{user_id}')
async def remove_user(user_id: UUID4) -> OutputSchema:
    deleted = user_service.remove_user(user_id)
    result = OutputSchema()

    if not deleted:
        result.error = "User not found!"

    return result


@router.get('/users')
async def get_all_users() -> OutputSchema:
    users = user_service.get_all_users()
    result = OutputSchema()

    if users:
        result.data = { "users": [{"id": user.id,
                                   "login": user.name,
                                   "height": user.height,
                                   "weight": user.weight} for user in users]}
    else:
        result.error = "User not found!"

    return result


@router.get('/users/{user_id}')
async def get_user(user_id: UUID4) -> OutputSchema:
    user = user_service.get_user(user_id)
    result = OutputSchema()

    if user:
        result.data = {
            "login": user.name,
            "height": user.height,
            "weight": user.weight
        }
    else:
        result.error = "User not found!"

    return result
