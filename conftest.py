import pytest


def pytest_addoption(parser):
    """добавляем параметры для командой строки"""

    parser.addoption("--url", action="store", default="https://ya.ru", help="this is request url")
    parser.addoption("--status_code", action="store", default="200", help="this is status code")


@pytest.fixture()
def url_param(request):
    """читаем url c командой строки"""

    return request.config.getoption("--url")


@pytest.fixture()
def status_code_param(request):
    """читаем status code c командой строки"""

    return request.config.getoption("--status_code")
