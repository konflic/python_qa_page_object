import pytest
import os

from selenium import webdriver

DRIVERS = os.path.expanduser("/Users/alicerossi/python_qa_page_object/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome")
    parser.addoption("--executor", "-E", default="local")
    parser.addoption("--url", "-U", default="http://192.168.1.38/")
    parser.addoption("--tolerance", type=int, default=3)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")
    common_caps = {"pageLoadStrategy": "eager"}

    driver = webdriver.Chrome(
        executable_path=f"{DRIVERS}/chromedriver",
        desired_capabilities=common_caps
        )

    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()

    driver.open = open
    driver.open()
    driver.t = tolerance

    return driver, url
