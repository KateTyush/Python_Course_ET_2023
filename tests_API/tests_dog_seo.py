import pytest
import requests

BASE_URL = 'https://dog.ceo/api'


def tests_get_random_image():
    response = requests.get(f'{BASE_URL}/breeds/image/random')
    assert response.status_code == 200
    assert response.json()['status'] == 'success'


def tests_get_multiple_random_images():
    response = requests.get(f'{BASE_URL}/breeds/image/random/5')
    assert response.status_code == 200
    assert len(response.json()['message']) == 5


def tests_get_list_all_breeds():
    response = requests.get(f'{BASE_URL}/breeds/list/all')
    assert response.status_code == 200
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize(("breed"),
                         ['hound', 'affenpinscher', 'greyhound'])
def tests_get_images_from_breed(breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/images')
    assert response.status_code == 200
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize(("breed"),
                         ['borzoi', 'chow', 'doberman'])
def tests_get_list_of_sub_breeds(breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/list')
    assert response.status_code == 200
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize(("breed"),
                         ['test', 'doberman2'])
def tests_get_list_of_nonexisting_sub_breeds_negative(breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/list')
    assert response.status_code == 404
    assert response.json()['status'] == 'error'
