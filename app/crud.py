import uuid
from datetime import datetime

from sqlalchemy import and_, desc
from sqlalchemy.orm import Session

from . import models, schemas
from .settings import LIMIT_DEFAULT


def get_makes(db: Session, skip: int = 0, limit: int = LIMIT_DEFAULT):
    return db.query(models.Make).offset(skip).limit(limit).all()


def get_models(db: Session, skip: int = 0, limit: int = LIMIT_DEFAULT):
    return db.query(models.Model).offset(skip).limit(limit).all()


def get_submodels(db: Session, skip: int = 0, limit: int = LIMIT_DEFAULT):
    return db.query(models.Submodel).offset(skip).limit(limit).all()


def get_cars(db: Session, skip: int = 0, limit: int = LIMIT_DEFAULT):
    return db.query(models.Car).offset(skip).limit(limit).all()


def filter_cars(db: Session,
                price_min: int, price_max: int,
                mileage_min: int, mileage_max: int,
                skip: int = 0, limit: int = LIMIT_DEFAULT):
    return db.query(models.Car).filter(
        and_(
            models.Car.price >= price_min,
            models.Car.price <= price_max,
            models.Car.mileage >= mileage_min,
            models.Car.mileage <= mileage_max,
        )
    ).order_by(desc(models.Car.updated_at)).offset(skip).limit(limit).all()


def create_car(db: Session, car: schemas.CarCreate):
    car_id = str(uuid.uuid4())
    created_at = datetime.utcnow().isoformat()
    updated_at = created_at
    db_car = models.Car(
        id=car_id,
        active=car.active,
        created_at=created_at,
        updated_at=updated_at,
        year=car.year,
        mileage=car.mileage,
        price=car.price,
        make_id=car.make_id,
        model_id=car.model_id,
        submodel_id=car.submodel_id,
        body_type=car.body_type,
        transmission=car.transmission,
        fuel_type=car.fuel_type,
        exterior_color=car.exterior_color
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
