from selenium.webdriver.common.by import By


class AlertElement:

    def __init__(self, driver):
        self.driver = driver

    @property
    def comparison(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "product comparison")

    @property
    def login(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, 'login')

    @property
    def cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "shopping cart")
