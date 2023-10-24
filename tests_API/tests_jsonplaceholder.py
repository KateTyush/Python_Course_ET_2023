import pytest
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'


def tests_create_resource():
    data = {"title": "test_1", "body": "test_2", "userId": 33}
    response = requests.post(f'{BASE_URL}', data=data)
    assert response.status_code == 201
    assert response.json()['title'] == 'test_1'
    assert response.json()['body'] == 'test_2'
    assert response.json()['userId'] == '33'


@pytest.mark.parametrize(("id"),
                         [3, 5])
def tests_get_resource(id):
    response = requests.get(f'{BASE_URL}/{id}')
    assert response.status_code == 200
    assert response.json()['id'] == id
    assert response.json()['userId'] == 1


@pytest.mark.parametrize(("title"),
                         ['First', 'second'])
def tests_change_resource(title):
    data = {"title": {title}}
    response = requests.patch(f'{BASE_URL}/1', data=data)
    assert response.status_code == 200
    assert response.json()['title'] == title


def tests_delete_resource():
    response = requests.delete(f'{BASE_URL}/2')
    assert response.status_code == 200
    assert response.json() == {}


def tests_get_nonexisting_resource():
    response = requests.get(f'{BASE_URL}/1234567')
    assert response.status_code == 404
    assert response.json() == {}
