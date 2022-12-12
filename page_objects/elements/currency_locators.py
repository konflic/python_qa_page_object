from selenium.webdriver.common.by import By


class CurrencyLocators:
    # Элементы валюты
    CURRENCY_BUTTON = (By.CLASS_NAME, 'btn-group')
    EURO_BUTTON = (By.NAME, 'EUR')
    POUND_BUTTON = (By.NAME, 'GBP')
    DOLLAR_BUTTON = (By.NAME, 'USD')
    ACTIVE_CURRENCY_EURO = (By.XPATH, "//strong[contains(text(),'€')]")
    ACTIVE_CURRENCY_POUND = (By.XPATH, "//strong[contains(text(),'£')]")
    ACTIVE_CURRENCY_DOLLAR = (By.XPATH, "//strong[contains(text(),'$')]")
    EURO_CURRENCY_IN_CART = (By.XPATH, "//span[contains(text(),'0 item(s) - 0.00€')]")
    DOLLAR_CURRENCY_IN_CART = (By.XPATH, "//span[contains(text(),'0 item(s) - $0.00')]")
    POUND_CURRENCY_IN_CART = (By.XPATH, "//span[contains(text(),'0 item(s) - £0.00')]")
