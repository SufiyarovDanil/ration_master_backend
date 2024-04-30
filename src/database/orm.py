from sqlalchemy import SmallInteger, VARCHAR, UUID, ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    name: Mapped[VARCHAR] = mapped_column(
        VARCHAR(32),
        nullable=False,
        unique=True,
        name='name'
    )
    password: Mapped[VARCHAR] = mapped_column(
        VARCHAR(64),
        nullable=False,
        name='password'
    )
    height: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        name='height'
    )
    weight: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        name='weight'
    )

class ProductModel(BaseModel):
    __tablename__ = 'product'

    id: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    name: Mapped[VARCHAR] = mapped_column(
        VARCHAR(64),
        nullable=False,
        unique=True,
        name='name'
    )
    protein: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        nullable=False,
        name='protein'
    )
    fat: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        nullable=False,
        name='weight'
    )
    carbohydrate: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        nullable=False,
        name='carbohydrate'
    )

class RationModel(BaseModel):
    __tablename__ = 'ration'

    id: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    user_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey('user.pk_id', ondelete='SET NULL'),
        nullable=False,
        name='fk_user_id'
    )
    product_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey('product.pk_id', ondelete='SET NULL'),
        nullable=False,
        name='fk_product_id'
    )
    product_gramm: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        nullable=False,
        name='product_gramm'
    )
    time_to_eat: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        nullable=False,
        name='time_to_eat'
    )
