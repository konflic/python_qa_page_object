import pytest
import os
import mysql.connector

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome")
    parser.addoption("--executor", "-E", default="127.0.0.1")
    parser.addoption("--url", "-U", default="http://demo.opencart.com")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """

    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")

    # https://www.selenium.dev/documentation/en/webdriver/page_loading_strategy/
    common_caps = {"pageLoadStrategy": "none"}

    if executor == "local":
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver",
            desired_capabilities=common_caps
        )
    else:

        desired_capabilities = {
            "browser": browser,
            **common_caps
        }

        driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor=f"http://{executor}:4444/wd/hub",
        )

    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.open = open
    driver.open()

    return driver


@pytest.fixture
def db_connection(request):
    connection = mysql.connector.connect(
        user='bn_opencart',
        password='',
        host='127.0.0.1',
        database='bitnami_opencart',
        port='3306'
    )
    request.addfinalizer(connection.close)
    return connection
