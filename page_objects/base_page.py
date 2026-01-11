from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator: tuple):
        ActionChains(self.driver).move_to_element(
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(locator))
        ).click().perform()
