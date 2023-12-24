from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class WishListPage(BasePage):

    def _product_name(self, product_name):
        return (By.XPATH, f"//*[@id='account-wishlist']//*[text()='{product_name}']")

    def wait_for_product_in_wish_list(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self._product_name(product_name)))
