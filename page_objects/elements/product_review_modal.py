from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductReviewModal:
    PRODUCT_NAME = (By.CSS_SELECTOR, "#post-product-comment-form p")

    def __init__(self, driver):
        self.driver = driver

    def verify_product_name(self, product_name):
        WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element(self.PRODUCT_NAME, product_name))
