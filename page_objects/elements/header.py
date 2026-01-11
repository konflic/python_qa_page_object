from selenium.webdriver.common.by import By


class Header:
    LOGIN_LINK = (By.CSS_SELECTOR, '[title="Log in to your customer account"]')

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element(*self.LOGIN_LINK).click()
