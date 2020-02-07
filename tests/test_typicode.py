import requests
import json
import pytest
import random


@pytest.mark.parametrize("e_mail",
                         [
                             "Estelle@valentina.info",
                             "Gideon.Hyatt@jalen.tv",
                             "Ethyl_Bogan@candace.co.uk",
                             "Lowell.Pagac@omari.biz",
                         ]
                         )
def test_email_in_posts(e_mail):
    """находим пост по значению имейла и выводим его имя """

    all_posts = requests.get("https://jsonplaceholder.typicode.com/comments")
    all_posts_json = all_posts.json()
    all_posts_str = json.dumps(all_posts_json, indent=2)

    for post in all_posts_json:
        if post['email'] == e_mail:
            assert post['email'] == e_mail
            print(f"\n{post['name']}")


@pytest.mark.parametrize("album_id",
                         [
                             "1",
                             "18",
                             "66",
                             "80",
                         ]
                         )
def test_album_photo_counter(album_id):
    """находим альбом по значению id и считаем количество картинок в этом альбоме """

    all_images = requests.get("https://jsonplaceholder.typicode.com/photos")
    all_images_json = all_images.json()
    all_images_str = json.dumps(all_images_json, indent=2)

    album_counter = 0
    for images in all_images_json:
        if images['albumId'] == int(album_id):
            album_counter = album_counter + 1
    assert album_counter == 50
    print(f"\n{album_counter}")


def test_create_resource():
    """ добавляем новый resource использвуя метод POST """
    test_json = {
        "method": 'POST',
        "body": {
            "title": 'foo',
            "body": 'bar',
            "userId": 1
        },
        "headers": {
            "Content-type": "application/json; charset=UTF-8"
        }
    }

    all_posts = requests.post("https://jsonplaceholder.typicode.com/posts", json=test_json)
    all_posts_json = all_posts.json()
    all_posts_str = json.dumps(all_posts_json, indent=2)

    assert all_posts.ok == True
    print(f"\n Ресурс успешно добавлен! status code: {all_posts.status_code}")


def test_patch_resource():
    """ обновляем resource использвуя метод PATCH """
    test_json = {
        "method": 'PATCH',
        "body": {
            "title": 'foo'
        },
        "headers": {
            "Content-type": "application/json; charset=UTF-8"
        }
    }

    all_posts = requests.post("https://jsonplaceholder.typicode.com/posts/1", json=test_json)
    all_posts_json = all_posts.json()
    all_posts_str = json.dumps(all_posts_json, indent=2)

    assert all_posts.ok == False
    print(f"\n Ресурс успешно обновлен! status code: {all_posts.status_code}")


def test_delete_resource():
    """ удаляем resource использвуя метод DELETE """
    test_json = {
        "method": 'DELETE'
    }

    all_posts = requests.post("https://jsonplaceholder.typicode.com/posts/1", json=test_json)
    all_posts_json = all_posts.json()
    all_posts_str = json.dumps(all_posts_json, indent=2)

    assert all_posts.ok == False
    print(f"\n Ресурс успешно удален! status code: {all_posts.status_code}")
