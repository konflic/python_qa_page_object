from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".buttons").find_element(By.LINK_TEXT, "Checkout").click()
