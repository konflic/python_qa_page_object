from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class ComparisonPage(BasePage):
    CONFIRM_BUTTON = By.CSS_SELECTOR, "#button-confirm"

    def _product_name(self, product_name):
        return (By.XPATH, f"//*[@id='product-compare']//*[text()='{product_name}']")

    def wait_for_product_in_comparison(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self._product_name(product_name)))

    def click_confirm(self):
        self.browser.find_element(*self.CONFIRM_BUTTON).click()
