import time
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_wish_list(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']").click()

    def add_to_comparison(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-original-title='Compare this Product']").click()

    def add_to_cart(self):
        time.sleep(1.5)  # Page loading problem
        self.driver.find_element_by_css_selector("#button-cart").click()
