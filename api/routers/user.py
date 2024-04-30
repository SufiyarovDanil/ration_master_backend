from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from api.schemas.user import UserCreateSchema, UserOutputSchema
from src import user as user_service

router: APIRouter = APIRouter(
    prefix='/api',
    tags=['Album']
)


@router.post('/user/create')
def create_user(user_data: UserCreateSchema) -> UserOutputSchema:
    user_id = user_service.create_user(
        user_data.name,
        user_data.password,
        user_data.height,
        user_data.weight
    )

    result = UserOutputSchema()

    if user_id:
        result.data = user_id
    else:
        result.error = "Failed to create user!"

    return result


@router.get('/user/{id}')
def get_user(id: UUID) -> JSONResponse:
    user = user_service.get_user(id)
    

    return JSONResponse(content=jsonable_encoder(user), status_code=200)
