from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_LINK = By.LINK_TEXT, "Checkout"

    def _product_name(self, product_name):
        return (By.XPATH, f"//*[@id='shopping-cart']//*[text()='{product_name}']")

    def click_checkout(self):
        self.get_element(self.CHECKOUT_LINK).click()

    def wait_for_product_in_cart(self, product_name):
        self.get_element(self._product_name(product_name))
