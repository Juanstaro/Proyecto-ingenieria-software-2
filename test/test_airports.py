import requests


def test_get_airports():

    response = requests.get(
        "http://localhost:8000/airports"
    )

    assert response.status_code == 200


def test_get_airport_by_id():

    response = requests.get(
        "http://localhost:8000/airports/1"
    )

    assert response.status_code == 200