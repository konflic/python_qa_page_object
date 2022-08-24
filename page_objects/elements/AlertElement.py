from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class AlertElement(BasePage):
    THIS = (By.CSS_SELECTOR, ".alert-success")
    COMPARISON = (By.LINK_TEXT, "product comparison")
    LOGIN = (By.LINK_TEXT, "login")
    CART = (By.LINK_TEXT, "shopping cart")

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.this = self.driver.find_element(*self.THIS)

    @property
    def comparison(self):
        return self.this.find_element(*self.COMPARISON)

    @property
    def login(self):
        return self.this.find_element(*self.LOGIN)

    @property
    def cart(self):
        return self.this.find_element(*self.CART)
