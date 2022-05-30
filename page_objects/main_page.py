from .base_page import BasePage
from page_objects.elements.currency_locators import CurrencyLocators


class MainPage(BasePage):

    def __init__(self, browser):
        self.browser, self.url = browser
        self.driver = self.browser
        self._config_logger()

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


    def check_currency_menu_and_cart(self, currency):
        currency_mapper = {
            "EURO": {
                "active_currency_list": CurrencyLocators.ACTIVE_CURRENCY_EURO,
                "currency_in_cart": CurrencyLocators.EURO_CURRENCY_IN_CART,
                "button_clicker": self.click_euro_currency_button
            },
            "DOLLAR": {
                "active_currency_list": CurrencyLocators.ACTIVE_CURRENCY_DOLLAR,
                "currency_in_cart": CurrencyLocators.DOLLAR_CURRENCY_IN_CART,
                "button_clicker": self.click_dollar_currency_button
            },
            "POUND": {
                "active_currency_list": CurrencyLocators.ACTIVE_CURRENCY_POUND,
                "currency_in_cart": CurrencyLocators.POUND_CURRENCY_IN_CART,
                "button_clicker": self.click_pound_currency_button
            }
        }
        currency_mapper.get(currency).get("button_clicker")()
        self._verify_element_presence(currency_mapper.get(currency).get("active_currency_list"))
        self._verify_element_presence(currency_mapper.get(currency).get("currency_in_cart"))