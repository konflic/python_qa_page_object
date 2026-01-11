from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-link-action='show-login-form']").click()

    def click_summary_products(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-target="#cart-summary-product-list"]').click()

    def verify_product_in_list(self, product_name):
        WebDriverWait(self.driver, 2).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.product-name"), product_name)
        )

    def verify_delivery_form(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delivery-address"))
        )
