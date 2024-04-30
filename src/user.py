from uuid import UUID

from sqlalchemy import select

from src.database import session_factory
from src.database.orm import UserModel


def create_user(name: str, password: str, height: int, weight: int) -> UUID | None:
    with session_factory() as session:
        new_user = UserModel(
            name=name,
            password=hash(password),
            height=height,
            weight=weight
        )

        session.add(new_user)

        query = select(UserModel).where(UserModel.name==name)
        result = session.execute(query)
    
    user: UserModel = result.one_or_none()

    if user:
        return user.id
    
    return None


def get_user(id: UUID) -> UserModel | None:
    with session_factory() as session:
        query = select(UserModel).where(UserModel.id==id)
        result = session.execute(query)
    
    return result.mappings().one_or_none()
