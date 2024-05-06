from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import select, delete
from sqlalchemy.orm import joinedload

from src.database import session_factory
from src.database.orm import RationModel, ProductModel


def create_ration(prod_id: UUID, product_gramm: int,
                  time_to_eat: datetime) -> UUID | None:
    with session_factory() as session:
        prod_exists: bool = (
            session.execute(
                select(ProductModel).where(ProductModel.id == prod_id)
            ).one_or_none() is not None
        )

        if not prod_exists:
            return None

        ration_id: UUID = uuid4()
        new_ration = RationModel(
            id=ration_id,
            product_id=prod_id,
            product_gramm=product_gramm,
            time_to_eat=time_to_eat
        )

        session.add(new_ration)

        query = select(RationModel).where(RationModel.id == ration_id)
        result = session.execute(query)
        session.commit()
    
    ration: RationModel = result.mappings().one_or_none()

    return ration_id if ration else None


def remove_ration(id: UUID) -> bool:
    with session_factory() as session:
        query = delete(RationModel).where(RationModel.id==id)
        session.execute(query)
        session.commit()


def get_ration(id: UUID) -> RationModel | None:
    with session_factory() as session:
        query = select(RationModel).where(RationModel.id==id).options(joinedload(RationModel.product))
        result = session.execute(query)
        ration = result.scalar()

    return ration


def get_all_rations() -> list[RationModel] | None:
    with session_factory() as session:
        query = select(RationModel).options(joinedload(RationModel.product))
        result = session.execute(query)
        rations = result.scalars().all()
    
    return rations
