from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CartPage(BasePage):
    BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")

    def click_checkout(self):
        self.element(self.BUTTONS).find_element(*self.CHECKOUT_LINK).click()
