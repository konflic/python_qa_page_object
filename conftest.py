import pytest
import mysql.connector

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome")
    parser.addoption("--url", "-U", default="http://localhost:8081")


@pytest.fixture()
def browser(request):
    """Фикстура инициализации браузера"""

    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        options=options,
    )

    request.addfinalizer(driver.quit)

    driver.url = url

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()
    driver.implicitly_wait(3)

    driver.open = open
    driver.open()

    return driver


@pytest.fixture()
def db_connection(request):
    connection = mysql.connector.connect(
        user="root",
        password="admin",
        host="localhost",
        database="prestashop",
        port="3306",
    )
    request.addfinalizer(connection.close)
    return connection


@pytest.fixture()
def clean_wishlist(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM ps_wishlist_product")
    db_connection.commit()
    cursor.close()
