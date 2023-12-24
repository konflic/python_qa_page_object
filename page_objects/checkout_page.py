from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_FORM = By.ID, "checkout-checkout"
    CHECKOUT_PAYMENT_FORM = By.ID, "checkout-payment-method"

    def click_login_page_link(self):
        self.browser.find_element(By.LINK_TEXT, "login page").click()

    def wait_page_load(self):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.CHECKOUT_FORM))

    def wait_payment_form(self):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.CHECKOUT_PAYMENT_FORM))
