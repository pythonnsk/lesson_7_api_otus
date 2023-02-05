import requests
import pytest
from api_test import configuration
from api_test.configuration import Endpoints


def test_get_all_brewery():
    response = requests.get(configuration.BREWERY_URL)
    data = response.json()
    print(data)
    assert response.status_code == 200


def test_get_random_brewbery():
    response = requests.get(configuration.BREWERY_URL + '/random')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1


@pytest.mark.parametrize("city", ["windsor", "killeshin", "houston", "williamsville"])
def test_get_brewery_by_city(city):
    response = requests.get(configuration.BREWERY_URL + f"?by_city={city}", params={'brewery': city})
    assert response.status_code == 200
    assert response.json()[0]["city"].lower() == city


@pytest.mark.parametrize("state", ["new york", "oregon", "minnesota", "texas"])
def test_get_brewery_by_state(state):
    response = requests.get(configuration.BREWERY_URL + f"?by_state={state}", params={'brewery': state})
    assert response.status_code == 200
    print(response.json())
    assert response.json()[0]["state"].lower() == state


def test_search_brewery():
    query = "minnesota"
    response = requests.get(configuration.BREWERY_URL + '/search' + f"?query={query}")
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0
