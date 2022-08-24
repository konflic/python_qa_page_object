from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class UserPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")
    WISH_LIST_LINK = (By.LINK_TEXT, 'Wish List')
    PAYMENT_FORM = ((By.ID, "payment-new"))

    def login(self, username, password):
        self.element(self.EMAIL_INPUT).send_keys(username)
        self.element(self.PASSWORD_INPUT).send_keys(password)
        self.element(self.LOGIN_BUTTON).click()

    def open_wish_list(self):
        self.element(self.WISH_LIST_LINK).click()

    def verify_payment_form(self):
        return self.element(self.PAYMENT_FORM)
