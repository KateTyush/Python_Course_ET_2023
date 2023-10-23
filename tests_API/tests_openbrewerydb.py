import json
import pytest
import requests

Base_URL = 'https://api.openbrewerydb.org/v1/breweries'


def tests_get_list_breweries():
    response = requests.get(f'{Base_URL}')
    assert response.status_code == 200
    assert len(json.loads(response.text)) == 50


def tests_get_quantity_breweries_per_page():
    response = requests.get(f'{Base_URL}?per_page=3')
    assert response.status_code == 200
    assert len(json.loads(response.text)) == 3


def tests_get_single_brewery():
    response = requests.get(f'{Base_URL}/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0')
    assert response.status_code == 200
    assert json.loads(response.text)['id'] == 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'


@pytest.mark.parametrize(("state"),
                         ['Colorado', 'California', 'Oklahoma'])
def tests_get_breweries_by_state(state):
    response = requests.get(f'{Base_URL}?by_state={state}')
    assert response.status_code == 200
    assert json.loads(response.text)[0]['state_province'] == state


@pytest.mark.parametrize(("type"),
                         ['micro', 'bar'])
def tests_get_breweries_by_type(type):
    response = requests.get(f'{Base_URL}?by_type={type}')
    assert response.status_code == 200
    assert json.loads(response.text)[0]['brewery_type'] == type
