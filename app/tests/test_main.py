from .fixtures_data import MAKE_FIXTURE_DATA, MODEL_FIXTURE_DATA, SUBMODEL_FIXTURE_DATA, CAR_FIXTURE_DATA


def test_list_makes(client, db_fixture):
    response = client.get("/makes/")
    assert response.status_code == 200, response.text
    assert len(response.json()) == len(MAKE_FIXTURE_DATA)


def test_list_models(client, db_fixture):
    response = client.get("/models/")
    assert response.status_code == 200, response.text
    assert len(response.json()) == len(MODEL_FIXTURE_DATA)


def test_list_submodels(client, db_fixture):
    response = client.get("/submodels/")
    assert response.status_code == 200, response.text
    assert len(response.json()) == len(SUBMODEL_FIXTURE_DATA)


def test_list_cars(client, db_fixture):
    response = client.get("/cars/")
    assert response.status_code == 200, response.text
    assert len(response.json()) == len(CAR_FIXTURE_DATA)


def test_filter_cars_bad_query(client, db_fixture):
    response = client.get("/cars/filter/")
    assert response.status_code == 422


def test_filter_cars_all_cars(client, db_fixture):
    response = client.get("/cars/filter/?price_min=0&price_max=100000&mileage_min=0&mileage_max=100000")
    assert response.status_code == 200, response.text
    assert len(response.json()) == len(CAR_FIXTURE_DATA)
    update_times = [c['updated_at'] for c in response.json()]
    assert update_times == sorted(update_times, reverse=True)


def test_filter_cars_one_car(client, db_fixture):
    response = client.get("/cars/filter/?price_min=0&price_max=5000&mileage_min=0&mileage_max=100000")
    assert response.status_code == 200, response.text
    assert len(response.json()) == 1


def test_create_car(client, db_fixture):
    # insert new car with the same values as first car in fixture data only different price
    car_json = CAR_FIXTURE_DATA[0]
    car_json['price'] = 1
    del car_json['id']

    response = client.post("/cars/", json=car_json)
    assert response.status_code == 200, response.text

    response = client.get("/cars/")
    assert len(response.json()) == len(CAR_FIXTURE_DATA) + 1
