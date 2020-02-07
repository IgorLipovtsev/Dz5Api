import requests
import json
import pytest
import random


@pytest.mark.parametrize("city_param",
                         [
                             "Anchorage",
                             "Tucson",
                             "Chandler",
                             "Williams",
                         ]
                         )
def test_exact_city_in_all_brewery(city_param):
    """смотрим список всех brewery для конкретного города """

    city_params = {'by_city': city_param}
    all_brewery_by_city = requests.get("https://api.openbrewerydb.org/breweries", params=city_params)
    all_brewery_json = all_brewery_by_city.json()
    all_brewery_str = json.dumps(all_brewery_json, indent=2)

    for brewery in all_brewery_json:
        if brewery['city'] != city_param:
            print(f"\nпохоже {brewery['city']} и {city_param} похожи, но это не то, что нам нужно, продолжаем искать")
            continue
        assert brewery['city'] == city_param



@pytest.mark.parametrize("state_param",
                         [
                             "Pennsylvania",
                             "New York",
                             "Arizona",
                             "Virginia",
                         ]
                         )
def test_exact_state_in_all_brewery(state_param):
    """смотрим список конкретного штата и сверяем количество """

    url_state = f"https://api.openbrewerydb.org/breweries?by_state={state_param}"
    all_brewery_by_state = requests.get(url_state)
    all_brewery_json = all_brewery_by_state.json()
    all_brewery_str = json.dumps(all_brewery_json, indent=2)

    for brewery in all_brewery_json:
        if brewery['state'] == "Pennsylvania":
            assert len(brewery['state']) == 12

        if brewery['state'] == "New York":
            assert len(brewery['state']) == 8

        if brewery['state'] == "Arizona":
            assert len(brewery['state']) == 7

        if brewery['state'] == "Virginia":
            assert len(brewery['state']) == 8

    print(f"{state_param} встречается {len(brewery['state'])} раз")


def test_search_dog_in_all_brewery():
    """ищем все встречающиеся переменнные со значением dog """

    search_params = {'query': 'dog'}
    all_brewery = requests.get("https://api.openbrewerydb.org/breweries/search", params=search_params)
    all_brewery_json = all_brewery.json()
    all_brewery_str = json.dumps(all_brewery_json, indent=2)

    for brewery in all_brewery_json:
        for item in brewery:
            if "Dog" in str(brewery[item]):
                assert "Dog" in str(brewery[item])
                print(brewery[item])
            elif "dog" in str(brewery[item]):
                assert "dog" in str(brewery[item])
                print(brewery[item])


def test_exact_state_in_all_brewery():
    """открываем 15 страницу и проверяем статус код """

    all_brewery = requests.get("https://api.openbrewerydb.org/breweries?page=15")
    all_brewery_json = all_brewery.json()
    all_brewery_str = json.dumps(all_brewery_json, indent=2)

    url_str = all_brewery.url
    assert "page=15" in url_str
    assert all_brewery.status_code == 200
    print(f"\n status code : {all_brewery.status_code}")


def test_exact_brewery_in_all_brewery():
    """открываем конкретную brewery в списке всех brewery """

    all_brewery = requests.get("https://api.openbrewerydb.org/breweries")
    one_brewery = requests.get("https://api.openbrewerydb.org/breweries/141")
    all_brewery_json = all_brewery.json()
    one_brewery_json = one_brewery.json()

    for brewery in all_brewery_json:
        if brewery['id'] == 141:
            assert brewery['id'] == 141
            break
    assert all_brewery.status_code == 200
    print(f"\n status code : {all_brewery.status_code}")
    print("нашли совпадение!")
