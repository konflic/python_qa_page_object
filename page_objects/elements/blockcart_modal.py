from selenium.webdriver.common.by import By


class BlockCartModal:
    GO_TO_CART = (By.CSS_SELECTOR, "#blockcart-modal a")

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(*self.GO_TO_CART).click()
