import datetime
import logging

import allure
import pytest
import os

from allure_commons.types import AttachmentType
from selenium import webdriver

DRIVERS = os.path.expanduser("/Users/alicerossi/python_qa_page_object/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome")
    parser.addoption("--executor", "-E", default="local")
    parser.addoption("--url", "-U", default="http://192.168.1.38/")
    parser.addoption("--tolerance", type=int, default=3)
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

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
        if request.node.rep_call.failed:
            # Make the screen-shot if test failed:
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(end)
    return driver, url


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig, request):
    props = {
        'Browser': request.config.getoption("--browser"),
        'Stand': 'Production',
        'executor': request.config.getoption("--executor")
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/tests/allure-results/environment.properties', 'w') as f:
        env_props = '\n'.join([f'{k}={v}' for k, v in props.items()])
        f.write(env_props)
