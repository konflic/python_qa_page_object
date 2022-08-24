import time

from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    WISH_LIST = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    COMPARE = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    CART = (By.CSS_SELECTOR, "#button-cart")

    def add_to_wish_list(self):
        self.element(self.WISH_LIST).click()

    def add_to_comparison(self):
        self.element(self.COMPARE).click()

    def add_to_cart(self):
        time.sleep(1.5)  # Page loading problem
        self.element(self.CART).click()
