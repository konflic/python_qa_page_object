from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class WishListPage(BasePage):

    def _product_name(self, product_name):
        return (By.XPATH, f"//*[@id='account-wishlist']//*[text()='{product_name}']")

    def wait_for_product_in_wish_list(self, product_name):
        self.get_element(self._product_name(product_name))
