MAKE_FIXTURE_DATA = [
  {
    'id': 'make1',
    'name': 'make1',
    'active': 't',
    'created_at': '2020-01-01 00:00:00+01',
    'updated_at': '2020-01-02 00:00:00+01'
  },
  {
    'id': 'make2',
    'name': 'make2',
    'active': 'f',
    'created_at': '2020-01-02 00:00:00+01',
    'updated_at': '2020-01-02 00:00:00+01'
  },
]


MODEL_FIXTURE_DATA = [
  {
    "id": "model1",
    "name": "model1",
    "active": "t",
    "make_id": "make1",
    "created_at": "2017-01-16 09:06:17+01",
    "updated_at": "2018-01-29 12:57:44.944+01",
  },
  {
    "id": "model2",
    "name": "model2",
    "active": "t",
    "make_id": "make1",
    "created_at": "2017-01-16 09:06:17+01",
    "updated_at": "2018-01-29 12:57:44.944+01",
  },
  {
    "id": "model3",
    "name": "model3",
    "active": "t",
    "make_id": "make2",
    "created_at": "2017-01-16 09:06:17+01",
    "updated_at": "2018-01-29 12:57:44.944+01",
  }
]


SUBMODEL_FIXTURE_DATA = [
  {
    "id": "submodel1",
    "name": "submodel1",
    "active": "f",
    "model_id": "model1",
    "created_at": "2017-05-02 14:09:24+02",
    "updated_at": "2017-05-08 09:00:04+02",
  },
  {
    "id": "submodel2",
    "name": "submodel2",
    "active": "t",
    "model_id": "model2",
    "created_at": "2017-05-02 14:09:24+02",
    "updated_at": "2017-05-08 09:00:04+02",
  },
  {
    "id": "submodel3",
    "name": "submodel3",
    "active": "t",
    "model_id": "model3",
    "created_at": "2017-05-02 14:09:24+02",
    "updated_at": "2017-05-02 14:09:24+02",
  }
]


CAR_FIXTURE_DATA = [
  {
    "id": "car1",
    "active": "t",
    "year": 2016,
    "mileage": 54089,
    "price": 35902,
    "make_id": "make1",
    "model_id": "model1",
    "submodel_id": "submodel1",
    "body_type": "",
    "transmission": "Automatic",
    "fuel_type": "Petrol",
    "exterior_color": "White",
    "created_at": "2018-11-28 00:07:55.609081+01",
    "updated_at": "2019-08-16 04:09:56.073615+02",
  },
  {
    "id": "car2",
    "active": "f",
    "year": 2000,
    "mileage": 20000,
    "price": 30000,
    "make_id": "make2",
    "model_id": "model3",
    "submodel_id": "submodel3",
    "body_type": "",
    "transmission": "Automatic",
    "fuel_type": "Diesel",
    "exterior_color": "Black",
    "created_at": "2018-10-28 00:07:55.609081+01",
    "updated_at": "2019-07-16 04:09:56.073615+02",
  },
  {
    "id": "car3",
    "active": "f",
    "year": 2020,
    "mileage": 2000,
    "price": 3000,
    "make_id": "make1",
    "model_id": "model2",
    "submodel_id": "submodel2",
    "body_type": "",
    "transmission": "Manual",
    "fuel_type": "Diesel",
    "exterior_color": "Orange",
    "created_at": "2018-10-28 00:07:55.609081+01",
    "updated_at": "2020-01-01 04:09:56.073615+02",
  },
]