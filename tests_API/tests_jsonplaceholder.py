import json
import pytest
import requests

Base_URL = 'https://jsonplaceholder.typicode.com/posts'


def tests_create_resource():
    data = {"title": "test_1", "body": "test_2", "userId": 33}
    response = requests.post(f'{Base_URL}', data=data)
    assert response.status_code == 201
    assert json.loads(response.text)['title'] == 'test_1'
    assert json.loads(response.text)['body'] == 'test_2'
    assert json.loads(response.text)['userId'] == '33'


@pytest.mark.parametrize(("id"),
                         [3, 5])
def tests_get_resource(id):
    response = requests.get(f'{Base_URL}/{id}')
    assert response.status_code == 200
    assert json.loads(response.text)['id'] == id
    assert json.loads(response.text)['userId'] == 1


@pytest.mark.parametrize(("title"),
                         ['First', 'second'])
def tests_change_resource(title):
    data = {"title": {title}}
    response = requests.patch(f'{Base_URL}/1', data=data)
    assert response.status_code == 200
    assert json.loads(response.text)['title'] == title


def tests_delete_resource():
    response = requests.delete(f'{Base_URL}/2')
    assert response.status_code == 200
    assert json.loads(response.text) == {}


def tests_get_nonexisting_resource():
    response = requests.get(f'{Base_URL}/1234567')
    assert response.status_code == 404
    assert json.loads(response.text) == {}
