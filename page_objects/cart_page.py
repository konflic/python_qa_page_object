from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CartPage(BasePage):
    PROCEED_TO_CHECKOUT = (By.XPATH, '//a[text()="Proceed to checkout"]')

    def click_proceed_to_checkout(self):
        self.driver.find_element(*self.PROCEED_TO_CHECKOUT).click()
