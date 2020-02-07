import requests
import json
import pytest
import random


@pytest.mark.parametrize("hound",
                         [
                             "afghan",
                             "basset",
                             "blood",
                             "english",
                             "ibizan",
                             "plott",
                             "walker"
                         ]
                         )
def test_all_hound(hound):
    """провепяем наличие всех видов собак породы hound"""

    response = requests.get('https://dog.ceo/api/breeds/list/all')
    all_breeds_json = response.json()
    all_breeds_str = json.dumps(all_breeds_json, indent=2)
    breed_hound = all_breeds_json["message"]["hound"]
    assert hound in breed_hound
    print(hound)


@pytest.mark.parametrize("breed",
                         [
                             "https://images.dog.ceo/breeds/hound-basset/n02088238_10932.jpg",
                             "https://images.dog.ceo/breeds/hound-blood/n02088466_6712.jpg",
                             "https://images.dog.ceo/breeds/hound-english/n02089973_255.jpg",
                             "https://images.dog.ceo/breeds/hound-walker/n02089867_1987.jpg",

                         ]
                         )
def test_random_in_all_images(breed):
    """проверяем что случайная картинка есть в общем списке всех изображений + наличие изображений из параметризации в общем списке всех изображений"""

    all_images = requests.get('https://dog.ceo/api/breed/hound/images')
    all_images_breed_json = all_images.json()
    all_images_str = json.dumps(all_images_breed_json, indent=2)

    random_image = requests.get('https://dog.ceo/api/breed/hound/images/random')
    random_image_json = random_image.json()

    assert random_image_json['message'] in all_images_str
    assert random_image_json['message'] in all_images_breed_json['message']

    assert breed in all_images_breed_json['message']


def test_response_random_breed():
    """генерируем ссылку для картинки случайной породы собаки и проверяем корректность запроса"""

    response = requests.get('https://dog.ceo/api/breeds/list/all')
    all_breeds_json = response.json()
    breed_hound = all_breeds_json["message"]

    random_breed = random.choice(list(breed_hound.keys()))
    url_dog = f"https://dog.ceo/api/breed/{random_breed}/images/random"
    response_random_breed = requests.get(url_dog)
    print(response_random_breed.url)
    assert response_random_breed.status_code == 200


def test_len_sub_breed():
    """проверям количество собак породу terrrier"""

    response = requests.get('https://dog.ceo/api/breed/terrier/list')
    all_sub_breeds_json = response.json()
    sub_breed_terrier = all_sub_breeds_json["message"]

    assert len(sub_breed_terrier) == 21
    print(f"количество видов собак данной породы: {len(sub_breed_terrier)}")


def test_wrong_request():
    """проверям что заведомо сломаная ссылка возвращает корректный респонс статус"""

    response = requests.get('https://dog.ceo/api/breed/terrier/list/new')
    print(f"status code for current request: {response.status_code}")

    assert response.ok == False
