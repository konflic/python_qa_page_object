from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    SUMMARY_PRODUCTS = (By.CSS_SELECTOR, '[data-target="#cart-summary-product-list"]')
    DELIVERY_FORM = (By.CSS_SELECTOR, "#delivery-address")
    PRODUCT_NAME = (By.CSS_SELECTOR, "span.product-name")
    LOGIN_SWITCHER = (By.CSS_SELECTOR, "[data-link-action='show-login-form']")

    def switch_to_login(self):
        self.driver.find_element(*self.LOGIN_SWITCHER).click()

    def click_summary_products(self):
        self.driver.find_element(*self.SUMMARY_PRODUCTS).click()

    def verify_product_in_list(self, product_name):
        WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element(self.PRODUCT_NAME, product_name))

    def verify_delivery_form(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.DELIVERY_FORM))
