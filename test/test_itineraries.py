import requests


def test_create_itinerary():

    data = {
        "user_name": "Juan",
        "departure_airport": 1,
        "arrival_airport": 2,
        "travel_date": "2026-06-01",
        "duration_minutes": 120
    }

    response = requests.post(
        "http://localhost:8001/itineraries",
        json=data
    )

    assert response.status_code == 200


def test_invalid_airport():

    data = {
        "user_name": "Juan",
        "departure_airport": 99999,
        "arrival_airport": 2,
        "travel_date": "2026-06-01",
        "duration_minutes": 120
    }

    response = requests.post(
        "http://localhost:8001/itineraries",
        json=data
    )

    assert response.status_code == 404