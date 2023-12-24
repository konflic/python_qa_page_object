from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, browser):
        self.browser = browser

    def click_login_page_link(self):
        self.browser.find_element(By.LINK_TEXT, "login page").click()

    def wait_page_load(self):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, "checkout-checkout")))

    def wait_payment_form(self):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, "checkout-payment-method")))
