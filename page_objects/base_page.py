import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging


class BasePage:
    def __init__(self, browser):
        self.browser, self.url = browser
        self._config_logger()

    def _config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.driver.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, self.browser.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.logger.info("found link: {}".format(link_text))

        except TimeoutException:
            raise AssertionError("Cant find elements by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
            self.logger.info("found element: {}".format(locator))
        except TimeoutException:
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    def _verify_element_absence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.invisibility_of_element_located(locator))
            self.logger.info("Did not find element: {}".format(locator))

        except TimeoutException:
            raise AssertionError("found elements by locator: {}".format(locator))

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()
        self.logger.info("Clicked element: {}".format(locator))

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)
        self.logger.info("Clicked element: {}".format(locator))

    def click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        self.logger.info("Clicked link: {}".format(link_text))
        return self

    def _send_keys(self, element, keys):
        element = self._element(element)
        element.send_keys(keys)
        self.logger.info("Wrote {} in {}".format(keys, element))

    def confirm_alert(self):
        obj = self.browser.switch_to.alert
        obj.accept()
        self.browser.refresh()
        self.logger.info("Confirmed Alert")
