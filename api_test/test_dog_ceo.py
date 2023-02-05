import requests
import pytest
from api_test import configuration


# получить список всех пород
def test_get_list_all_breeds():
    response = requests.get(url=configuration.DOG_URL + '/breeds/list/all')
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) != 0


# получить одно случайное изображение
def test_get_single_random_image():
    response = requests.get(url=configuration.DOG_URL + '/breeds/image/random')
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"


# получить случайное изображение из коллекции подпород
def test_get_single_random_image_sub_breed():
    response = requests.get(url=configuration.DOG_URL + '/breed/hound/afghan/images/random')
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"


# получить несколько случайных изображений
@pytest.mark.parametrize("n", [1, 25, 50])
def test_get_multiple_random_images(n):
    response = requests.get(f"{configuration.DOG_URL}/breeds/image/random/{n}")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
    assert len(data["message"]) == n


# получить массив всех изображений из породы
@pytest.mark.parametrize("breed", ["bulldog", "hound", "corgi"])
def test_get_all_images_by_breed(breed):
    response = requests.get(f"{configuration.DOG_URL}/breed/{breed}/images")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
