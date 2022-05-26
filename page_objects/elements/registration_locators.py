from selenium.webdriver.common.by import By

from ..base_page import BasePage


class RegisterLocators(BasePage):
    INPUT_USERNAME = (By.ID, 'input-username')
    MY_ACCOUNT_BUTTON = (By.XPATH, "//a[@title='My Account']")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Register')]")
    NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    PHONE_FIELD = (By.ID, "input-telephone")
    PASS_FIELD = (By.ID, 'input-password')
    PASS_CONFIRM = (By.ID, 'input-confirm')
    PRIVACY_POLICY = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.XPATH, "//input[@type='submit']")
    ACCOUNT_CREATED = (By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def login_with(self, username, password):
        self._element(self.INPUT_EMAIL).send_keys(username)
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._element(self.LOGIN_BUTTON).click()
