from selenium.webdriver.common.by import By
from .base_page import BasePage
from .elements.registration_locators import RegisterLocators


class UserRegisterPage(BasePage):

    def open_register_page(self):
        self._click(RegisterLocators.MY_ACCOUNT_BUTTON)
        self._click(RegisterLocators.REGISTER_BUTTON)
        self._verify_element_presence(RegisterLocators.NAME_FIELD)

    def __init__(self, browser):
        super().__init__(browser)
        self.open_register_page()

    def input_name(self, name):
        self._click(RegisterLocators.NAME_FIELD)
        self._send_keys(RegisterLocators.NAME_FIELD, name)

    def input_last_name(self, last_name):
        self._click(RegisterLocators.LAST_NAME_FIELD)
        self._send_keys(RegisterLocators.LAST_NAME_FIELD, last_name)

    def input_email(self, email):
        self._click(RegisterLocators.EMAIL_FIELD)
        self._send_keys(RegisterLocators.EMAIL_FIELD, email)

    def input_phone_number(self, phone_number):
        self._click(RegisterLocators.PHONE_FIELD)
        self._send_keys(RegisterLocators.PHONE_FIELD, phone_number)

    def input_password(self, password):
        self._click(RegisterLocators.PASS_FIELD)
        self._send_keys(RegisterLocators.PASS_FIELD, password)
        self._click(RegisterLocators.PASS_CONFIRM)
        self._send_keys(RegisterLocators.PASS_CONFIRM, password)

    def confirm_privacy_policy(self):
        self._click(RegisterLocators.PRIVACY_POLICY)

    def click_continue(self):
        self._click(RegisterLocators.CONTINUE_BUTTON)

    def check_registration_success(self):
        self._verify_element_presence(RegisterLocators.ACCOUNT_CREATED)