from selenium.webdriver.common.by import By


class SignInModal:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element(By.CSS_SELECTOR, '.wishlist-login .wishlist-modal a').click()
