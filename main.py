from fastapi import FastAPI

from api.routers.user import router as user_router


app: FastAPI = FastAPI(
    title='Ration master API',
    swagger_ui_parameters={
        'displayRequestDuration': True,
        'defaultModelsExpandDepth': 0
    })

app.include_router(user_router)
