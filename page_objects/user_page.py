from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#form-login button").click()

    def wait_logged_in(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
