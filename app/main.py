from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .settings import LIMIT_DEFAULT

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/makes/", response_model=List[schemas.Make])
def read_makes(skip: int = 0, limit: int = LIMIT_DEFAULT, db: Session = Depends(get_db)):
    makes = crud.get_makes(db, skip=skip, limit=limit)
    return makes


@app.get("/models/", response_model=List[schemas.Model])
def read_models(skip: int = 0, limit: int = LIMIT_DEFAULT, db: Session = Depends(get_db)):
    models_list = crud.get_models(db, skip=skip, limit=limit)
    return models_list


@app.get("/submodels/", response_model=List[schemas.Submodel])
def read_submodels(skip: int = 0, limit: int = LIMIT_DEFAULT, db: Session = Depends(get_db)):
    submodels = crud.get_submodels(db, skip=skip, limit=limit)
    return submodels


@app.get("/cars/", response_model=List[schemas.Car])
def read_cars(skip: int = 0, limit: int = LIMIT_DEFAULT, db: Session = Depends(get_db)):
    cars = crud.get_cars(db, skip=skip, limit=limit)
    return cars


@app.get("/cars/filter/", response_model=List[schemas.Car])
def filter_cars(
        skip: int = 0,
        limit: int = LIMIT_DEFAULT,
        price_min: int = Query(..., title="Minimum price", ge=0),
        price_max: int = Query(..., title="Maximum price", ge=0),
        mileage_min: int = Query(..., title="Minimum mileage", ge=0),
        mileage_max: int = Query(..., title="Maximum mileage", ge=0),
        db: Session = Depends(get_db)
):
    if price_min is not None and price_max is not None:
        if price_min > price_max:
            raise HTTPException(status_code=400, detail="Maximum price should be larger than minimum")
    if mileage_min is not None and mileage_max is not None:
        if mileage_min > mileage_max:
            raise HTTPException(status_code=400, detail="Maximum mileage should be larger than minimum")
    cars = crud.filter_cars(
        db,
        price_min=price_min, price_max=price_max, mileage_min=mileage_min, mileage_max=mileage_max,
        skip=skip, limit=limit
    )
    return cars


@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db=db, car=car)
