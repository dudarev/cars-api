from typing import List, Optional, Literal

from pydantic import BaseModel, conint


class CommonBase(BaseModel):
    id: str
    created_at: str
    updated_at: str
    active: str


class Make(CommonBase):
    name: str

    class Config:
        orm_mode = True


class ModelBase(BaseModel):
    name: str
    active: Optional[str] = None
    make_id: str


class Model(ModelBase):
    id: str
    created_at: str
    updated_at: str
    make_name: Optional[str]

    class Config:
        orm_mode = True


class Submodel(BaseModel):
    id: str
    name: str
    active: Optional[str] = None
    model_id: str
    created_at: str
    updated_at: str
    model_name: Optional[str]

    class Config:
        orm_mode = True


class CarCreate(BaseModel):
    active: Literal['t', 'f'] = 't'
    year: conint(ge=1900)
    mileage: conint(ge=0)
    price: conint(ge=0)
    make_id: str
    model_id: str
    submodel_id: str
    body_type: str
    transmission: str
    fuel_type: str
    exterior_color: str


class Car(CarCreate):
    id: str
    created_at: str
    updated_at: str
    make: Optional[str]
    model: Optional[str]
    submodel: Optional[str]

    class Config:
        orm_mode = True
