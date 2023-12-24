from selenium.webdriver.common.by import By


class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#form-login button").click()
