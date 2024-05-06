from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from api.routers.product import router as prod_router
from api.routers.ration import router as ration_router
from api.schemas import OutputSchema
from src.database.orm import create_db


async def valid_data_exc_handler(
        request: Request,
        exc: RequestValidationError):
    """
    Кастомный хэндлер для ошибок валидации входных данных.

    Нужен для соблюдения общего формата ответа.

    """
    
    error = exc.errors()[0]

    content: OutputSchema = OutputSchema(
        data={'arg': error['loc']},
        error=error["msg"]
    )

    return JSONResponse(jsonable_encoder(content))


app: FastAPI = FastAPI(
    title='Ration master API',
    swagger_ui_parameters={'displayRequestDuration': True}
)

app.include_router(prod_router)
app.include_router(ration_router)
app.add_exception_handler(RequestValidationError, valid_data_exc_handler)

create_db()
