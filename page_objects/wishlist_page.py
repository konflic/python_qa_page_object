from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class WishlistPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".wishlist-product-title")

    def verify_product_in_wishlist(self, product_name):
        WebDriverWait(self.driver, 2).until(
            EC.text_to_be_present_in_element(self.PRODUCT_TITLE, product_name)
        )
