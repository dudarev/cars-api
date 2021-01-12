from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from .database import Base


class CommonFieldsMixin:
    id = Column(String, primary_key=True, index=True)
    active = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


class Make(CommonFieldsMixin, Base):
    __tablename__ = "make"
    name = Column(String)
    models = relationship("Model", back_populates="make")
    cars = relationship("Car", back_populates="make_obj")


class Model(CommonFieldsMixin, Base):
    __tablename__ = "model"
    name = Column(String)
    make_id = Column(String, ForeignKey('make.id'))
    make = relationship("Make", back_populates="models")
    submodels = relationship("Submodel", back_populates="model")
    cars = relationship("Car", back_populates="model_obj")
    make_name = association_proxy('make', 'name')


class Submodel(CommonFieldsMixin, Base):
    __tablename__ = "submodel"
    name = Column(String)
    model_id = Column(String, ForeignKey('model.id'))
    model = relationship("Model", back_populates="submodels")
    cars = relationship("Car", back_populates="submodel_obj")
    model_name = association_proxy('model', 'name')


class Car(CommonFieldsMixin, Base):
    __tablename__ = "car"
    year = Column(Integer)
    mileage = Column(Integer)
    price = Column(Integer)
    make_id = Column(String, ForeignKey('make.id'))
    model_id = Column(String, ForeignKey('model.id'))
    submodel_id = Column(String, ForeignKey('submodel.id'))
    body_type = Column(String)
    transmission = Column(String)
    fuel_type = Column(String)
    exterior_color = Column(String)
    make_obj = relationship("Make", back_populates="cars")
    model_obj = relationship("Model", back_populates="cars")
    submodel_obj = relationship("Submodel", back_populates="cars")
    make = association_proxy('make_obj', 'name')
    model = association_proxy('model_obj', 'name')
    submodel = association_proxy('submodel_obj', 'name')
