from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ComparisonPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to Cart']")
    CONTENT = (By.CSS_SELECTOR, "#content")

    def add_to_cart(self):
        self.element(self.CONTENT).find_element(*self.ADD_TO_CART).click()
