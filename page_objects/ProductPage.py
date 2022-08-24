import time
from selenium.webdriver.common.by import By


class ProductPage:
    WISH_LIST = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    COMPARE = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    CART = (By.CSS_SELECTOR, "#button-cart")

    def __init__(self, driver):
        self.driver = driver

    def add_to_wish_list(self):
        self.driver.find_element(*self.WISH_LIST).click()

    def add_to_comparison(self):
        self.driver.find_element(*self.COMPARE).click()

    def add_to_cart(self):
        time.sleep(1.5)  # Page loading problem
        self.driver.find_element(*self.CART).click()
