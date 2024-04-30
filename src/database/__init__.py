from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase

from config import get_database_url


class BaseModel(DeclarativeBase):
    pass

engine: Engine = create_engine(
    url=get_database_url(),
    echo=True
)
