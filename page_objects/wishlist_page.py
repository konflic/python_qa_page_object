from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class WishlistPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".wishlist-product-title")

    def verify_product_in_wishlist(self, product_name):
        self.wait_text_in_element(self.PRODUCT_TITLE, product_name)
