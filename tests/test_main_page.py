import pytest

from page_objects.main_page import MainPage


@pytest.mark.parametrize('currency', ['DOLLAR', 'EURO', 'POUND'])
def test_currency(browser, currency):
    main_page = MainPage(browser)

    main_page.check_currency_menu_and_cart(currency)
