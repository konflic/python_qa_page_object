from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#button-cart"
    ADD_TO_COMPARISON_BUTTON = By.CSS_SELECTOR, "[title='Compare this Product']"
    ADD_TO_WISH_LIST_BUTTON = By.CSS_SELECTOR, "[title='Add to Wish List']"

    def add_to_cart(self):
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()

    def add_to_comparison(self):
        self.browser.find_element(*self.ADD_TO_COMPARISON_BUTTON).click()

    def add_to_wish_list(self):
        self.browser.find_element(*self.ADD_TO_WISH_LIST_BUTTON).click()
