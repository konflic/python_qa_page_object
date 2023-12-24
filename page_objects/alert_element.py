from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))

    @property
    def login(self):
        return self.alert.find_element(By.LINK_TEXT, "login")

    @property
    def shopping_cart(self):
        return self.alert.find_element(By.LINK_TEXT, "shopping cart")

    @property
    def comparison(self):
        return self.alert.find_element(By.LINK_TEXT, "product comparison")
