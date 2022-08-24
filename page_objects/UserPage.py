from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[value=Login]").click()

    def open_wish_list(self):
        self.driver.find_element(By.LINK_TEXT, 'Wish List').click()

    def verify_payment_form(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))

    def verify_product_item(self, product_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
