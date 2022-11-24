import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.elements.registration_locators import RegisterLocators


class UserRegisterPage(BasePage):

    @allure.step('открываем страничку регистрации')
    def open_register_page(self):
        self._click(RegisterLocators.MY_ACCOUNT_BUTTON)
        self._click(RegisterLocators.REGISTER_BUTTON)
        self._verify_element_presence(RegisterLocators.NAME_FIELD)

    def __init__(self, browser):
        self.browser, self.url = browser
        self.driver = self.browser
        self._config_logger()
        self.open_register_page()

    @allure.step('вводим имя')
    def input_name(self, name):
        self._click(RegisterLocators.NAME_FIELD)
        self._send_keys(RegisterLocators.NAME_FIELD, name)

    @allure.step('вводим фамилию')
    def input_last_name(self, last_name):
        self._click(RegisterLocators.LAST_NAME_FIELD)
        self._send_keys(RegisterLocators.LAST_NAME_FIELD, last_name)

    @allure.step('вводим почту')
    def input_email(self, email):
        self._click(RegisterLocators.EMAIL_FIELD)
        self._send_keys(RegisterLocators.EMAIL_FIELD, email)

    @allure.step('вводим телефон')
    def input_phone_number(self, phone_number):
        self._click(RegisterLocators.PHONE_FIELD)
        self._send_keys(RegisterLocators.PHONE_FIELD, phone_number)

    @allure.step('вводим и подтверждаем пароль')
    def input_password(self, password):
        self._click(RegisterLocators.PASS_FIELD)
        self._send_keys(RegisterLocators.PASS_FIELD, password)
        self._click(RegisterLocators.PASS_CONFIRM)
        self._send_keys(RegisterLocators.PASS_CONFIRM, password)
        self.logger.info("ввожу пароль")

    @allure.step('подтверждаем')
    def confirm_privacy_policy(self):
        self._click(RegisterLocators.PRIVACY_POLICY)

    @allure.step('кликаем на далее')
    def click_continue(self):
        self._click(RegisterLocators.CONTINUE_BUTTON)

    @allure.step('проверяем регистрацию')
    def check_registration_success(self):
        self._verify_element_presence(RegisterLocators.ACCOUNT_CREATED)