from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    SUMMARY_PRODUCTS = (By.CSS_SELECTOR, '[data-target="#cart-summary-product-list"]')
    DELIVERY_FORM = (By.CSS_SELECTOR, "#delivery-address")
    PRODUCT_NAME = (By.CSS_SELECTOR, "span.product-name")
    LOGIN_SWITCHER = (By.CSS_SELECTOR, "[data-link-action='show-login-form']")

    def switch_to_login(self):
        self.click(self.LOGIN_SWITCHER)

    def click_summary_products(self):
        self.click(self.SUMMARY_PRODUCTS)

    def verify_product_in_list(self, product_name):
        self.wait_text_in_element(self.PRODUCT_NAME, product_name)

    def verify_delivery_form(self):
        return self.wait_element_visible(self.DELIVERY_FORM)
