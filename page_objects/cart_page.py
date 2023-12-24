from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_LINK = By.LINK_TEXT, "Checkout"

    def _product_name(self, product_name):
        return (By.XPATH, f"//*[@id='shopping-cart']//*[text()='{product_name}']")

    def click_checkout(self):
        self.browser.find_element(*self.CHECKOUT_LINK).click()

    def wait_for_product_in_cart(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self._product_name(product_name)))
