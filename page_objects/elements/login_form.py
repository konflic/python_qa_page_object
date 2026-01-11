from selenium.webdriver.common.by import By


class LoginForm:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password, submit_element):
        self.driver.find_element(By.CSS_SELECTOR, "#login-form #field-email").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#login-form #field-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, f"#login-form {submit_element}").click()
