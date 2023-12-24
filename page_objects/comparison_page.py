from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComparisonPage:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_product_in_comparison(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))

    def click_confirm(self):
        self.browser.find_element(By.CSS_SELECTOR, "#button-confirm").click()
