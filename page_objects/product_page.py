from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "#button-cart").click()

    def add_to_comparison(self):
        self.browser.find_element(By.CSS_SELECTOR, "[title='Compare this Product']").click()

    def add_to_wish_list(self):
        self.browser.find_element(By.CSS_SELECTOR, "[title='Add to Wish List']").click()
