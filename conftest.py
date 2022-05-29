import datetime
import logging

import pytest
import os

from selenium import webdriver

DRIVERS = os.path.expanduser("/Users/alicerossi/python_qa_page_object/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome")
    parser.addoption("--executor", "-E", default="local")
    parser.addoption("--url", "-U", default="http://192.168.1.38/")
    parser.addoption("--tolerance", type=int, default=3)
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")
    log_level = request.config.getoption("--log_level")
    common_caps = {"pageLoadStrategy": "eager"}

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    driver = webdriver.Chrome(
        executable_path=f"{DRIVERS}/chromedriver",
        desired_capabilities=common_caps
    )

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()

    driver.open = open
    driver.open()
    driver.t = tolerance

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def end():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(end)

    return driver, url
