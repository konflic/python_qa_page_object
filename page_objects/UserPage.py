from selenium.webdriver.common.by import By


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[value=Login]").click()

    def open_wish_list(self):
        self.driver.find_element(By.LINK_TEXT, 'Wish List').click()
