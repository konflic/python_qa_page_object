import allure
import pytest

from page_objects.main_page import MainPage


@allure.story('проверка валюты')
@pytest.mark.parametrize('currency', ['DOLLAR', 'EURO', 'POUND'])
def test_currency(browser, currency):
    with allure.step('открываем страницу'):
        main_page = MainPage(browser)

    with allure.step('кликаем на валюту, проверяем изменения'):
        main_page.check_currency_menu_and_cart(currency)


