from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComparisonPage:
    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to Cart']")
    CONTENT = (By.CSS_SELECTOR, "#content")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(*self.CONTENT).find_element(*self.ADD_TO_CART).click()

    def verify_product_item(self, product_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
