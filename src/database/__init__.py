from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import get_database_url


class BaseORM(DeclarativeBase):
    pass


engine: Engine = create_engine(url=get_database_url())

session_factory: sessionmaker[Session] = sessionmaker(engine)
