from selenium.webdriver.common.by import By


class ProductPage:
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#button-cart"
    ADD_TO_COMPARISON_BUTTON = By.CSS_SELECTOR, "[title='Compare this Product']"
    ADD_TO_WISH_LIST_BUTTON = By.CSS_SELECTOR, "[title='Add to Wish List']"

    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self):
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()

    def add_to_comparison(self):
        self.browser.find_element(*self.ADD_TO_COMPARISON_BUTTON).click()

    def add_to_wish_list(self):
        self.browser.find_element(*self.ADD_TO_WISH_LIST_BUTTON).click()
