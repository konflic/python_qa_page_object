import pytest
import os

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--url", "-U", default="http://demo.opencart.com")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    url = request.config.getoption("--url")

    # https://www.selenium.dev/documentation/en/webdriver/page_loading_strategy/
    common_caps = {"pageLoadStrategy": "none"}

    driver = webdriver.Chrome(
        executable_path=f"{DRIVERS}/chromedriver",
        desired_capabilities=common_caps
    )

    request.addfinalizer(driver.quit)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)

    return driver
