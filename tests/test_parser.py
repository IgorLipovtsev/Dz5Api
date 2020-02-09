import pytest
import requests


def test_url_status_code_response(url_param, status_code_param):
    """принимает значения параметров, введенных в командной строке и прверяем их корректность"""

    response = requests.get(url_param)

    if response.status_code == int(status_code_param):
        print("переданнные параметры в строке совпадают с реальными!")
        print(
            f"\nпереданный status code для {url_param} = {status_code_param},  полученный в запросе: {response.status_code}"
        )

    else:
        print(f"\nпроверьте правильность одного из параметров!")
        print(
            f"\nпереданный status code для {url_param} = {status_code_param},  полученный в запросе: {response.status_code}"
        )
