import requests
import pytest
from api_test import configuration


def test_post():
    response = requests.post(configuration.JSONPLACEHOLDER_URL + "/posts")
    assert response.status_code == 201
    assert response.json()["id"] == 101


def test_delete():
    response = requests.delete(configuration.JSONPLACEHOLDER_URL + "/posts/1")
    print(response.json())
    assert response.status_code == 200


def test_get_albums_photo():
    album_id = 6
    response = requests.get(f"{configuration.JSONPLACEHOLDER_URL}/albums/{album_id}/photos/")
    data = response.json()
    for i in data:
        assert i["albumId"] == album_id


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_id(post_id):
    response = requests.get(f"{configuration.JSONPLACEHOLDER_URL}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id


@pytest.mark.parametrize("by_params", ["photos", "albums"])
def test_get_by_more_params(by_params):
    response = requests.get(f"{configuration.JSONPLACEHOLDER_URL}/{by_params}", params=by_params)
    assert response.status_code == 200
