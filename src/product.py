from uuid import UUID, uuid4

from sqlalchemy import select, delete

from src.database import session_factory
from src.database.orm import ProductModel


def create_product(name: str, protein: int, fat: int,
                   carbohydrate: int) -> UUID | None:
    with session_factory() as session:
        product_id: UUID = uuid4()
        new_prod = ProductModel(
            id=product_id,
            name=name,
            protein=protein,
            fat=fat,
            carbohydrate=carbohydrate
        )

        session.add(new_prod)

        query = select(ProductModel).where(ProductModel.id == product_id)
        result = session.execute(query)
        session.commit()
    
    prod: ProductModel = result.mappings().one_or_none()

    return product_id if prod else None


def remove_product(id: UUID) -> bool:
    with session_factory() as session:
        query = delete(ProductModel).where(ProductModel.id==id)
        session.execute(query)
        session.commit()


def get_product(id: UUID) -> ProductModel | None:
    with session_factory() as session:
        query = select(ProductModel).where(ProductModel.id==id)
        result = session.execute(query)
        prod = result.scalar()

    return prod


def get_all_products() -> list[ProductModel] | None:
    with session_factory() as session:
        query = select(ProductModel)
        result = session.execute(query)
        prods = result.scalars().all()
    
    return prods
