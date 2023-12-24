import pytest
import os
import mysql.connector

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--url", "-U", default="http://demo.opencart.com")


@pytest.fixture
def browser(request):
    url = request.config.getoption("--url")

    driver = webdriver.Chrome(
        service=ChromeService()
    )

    request.addfinalizer(driver.quit)

    driver.maximize_window()

    driver.get(url)

    return driver


@pytest.fixture(scope="session")
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
