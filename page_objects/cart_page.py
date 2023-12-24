from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, browser):
        self.browser = browser

    def click_checkout(self):
        self.browser.find_element(By.LINK_TEXT, "Checkout").click()

    def wait_for_product_in_cart(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='shopping-cart']//*[text()='{product_name}']")))
