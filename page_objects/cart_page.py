from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, '//a[text()="Proceed to checkout"]').click()
