from uuid import UUID, uuid4

from sqlalchemy import select, delete

from src.database import session_factory
from src.database.orm import UserModel


def create_user(name: str, password: str, height: int,
                weight: int) -> UUID | None:
    try:
        with session_factory() as session:
            user_id: UUID = uuid4()
            new_user = UserModel(
                id=user_id,
                name=name,
                password=hash(password),
                height=height,
                weight=weight
            )

            session.add(new_user)

            query = select(UserModel).where(UserModel.id==user_id)
            result = session.execute(query)
            session.commit()
    except Exception:
        return None
    
    user: UserModel = result.mappings().one_or_none()

    if user:
        return user_id
    
    return None


def remove_user(id: UUID) -> bool:
    with session_factory() as session:
        query = delete(UserModel).where(UserModel.id==id)
        session.execute(query)
        session.commit()


def get_user(id: UUID) -> UserModel | None:
    with session_factory() as session:
        query = select(UserModel).where(UserModel.id==id)
        result = session.execute(query)
        user = result.scalar()

    return user


def get_all_users() -> list[UserModel] | None:
    with session_factory() as session:
        query = select(UserModel)
        result = session.execute(query)
        users = result.scalars().all()
    
    return users
