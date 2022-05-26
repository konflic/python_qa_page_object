from page_objects.main_page import MainPage


def test_currency(browser):
    main_page = MainPage(browser)

    main_page.click_euro_currency_button()
    main_page.check_euro_currency_menu_and_cart()

    main_page.click_dollar_currency_button()
    main_page.check_dollar_currency_menu_and_cart()

    main_page.click_pound_currency_button()
    main_page.check_pound_currency_menu_and_cart()


