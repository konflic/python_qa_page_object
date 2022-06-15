import logging

import allure

from page_objects.base_page import BasePage
from page_objects.elements.registration_locators import RegisterLocators


class AdminPage(BasePage):
    def __init__(self, browser):
        self.browser, self.url = browser
        self.driver = self.browser
        self._config_logger()
        self.browser.get(self.url + '/admin')
        self.check_admin_page()

    @allure.step('проверяем логин в админку')
    def check_admin_page(self):
        self._verify_element_presence(RegisterLocators.INPUT_USERNAME)

    @allure.step('вводим username')
    def input_username(self, username):
        self._send_keys(RegisterLocators.INPUT_USERNAME, username)

    @allure.step('вводим пароль')
    def input_password(self, password):
        self._click(RegisterLocators.PASS_FIELD)
        self._send_keys(RegisterLocators.PASS_FIELD, password)

    @allure.step('логинимся в админку')
    def login_to_admin(self):
        self.input_username('user')
        self.input_password('bitnami')
        self._click(RegisterLocators.LOGIN_BUTTON)
