from .base_page import BasePage
from page_objects.elements.currency_locators import CurrencyLocators


class MainPage(BasePage):

    # взаимодействие с валютным списком
    def click_euro_currency_button(self):
        self._click(CurrencyLocators.CURRENCY_BUTTON)
        self._click(CurrencyLocators.EURO_BUTTON)

    def click_dollar_currency_button(self):
        self._click(CurrencyLocators.CURRENCY_BUTTON)
        self._click(CurrencyLocators.DOLLAR_BUTTON)

    def click_pound_currency_button(self):
        self._click(CurrencyLocators.CURRENCY_BUTTON)
        self._click(CurrencyLocators.POUND_BUTTON)

    # проверки валюты в корзине и верхнем валютном меню

    def check_euro_currency_menu_and_cart(self):
        self._verify_element_presence(CurrencyLocators.ACTIVE_CURRENCY_EURO)
        self._verify_element_presence(CurrencyLocators.EURO_CURRENCY_IN_CART)

    def check_dollar_currency_menu_and_cart(self):
        self._verify_element_presence(CurrencyLocators.ACTIVE_CURRENCY_DOLLAR)
        self._verify_element_presence(CurrencyLocators.DOLLAR_CURRENCY_IN_CART)

    def check_pound_currency_menu_and_cart(self):
        self._verify_element_presence(CurrencyLocators.ACTIVE_CURRENCY_POUND)
        self._verify_element_presence(CurrencyLocators.POUND_CURRENCY_IN_CART)
