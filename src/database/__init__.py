from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase

from config import get_database_url


class BaseModel(DeclarativeBase):
    pass


async_engine: Engine = create_engine(
    url=get_database_url(),
    echo=True
)

async_session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(async_engine)
