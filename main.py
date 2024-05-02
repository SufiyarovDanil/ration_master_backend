from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from api.routers.user import router as user_router
from api.schemas import OutputSchema


async def validation_exception_handler(
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
    swagger_ui_parameters={
        'displayRequestDuration': True,
        'defaultModelsExpandDepth': 0
    })

app.include_router(user_router)
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)
