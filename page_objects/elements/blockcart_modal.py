from selenium.webdriver.common.by import By


class BlockCartModal:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#blockcart-modal a").click()
