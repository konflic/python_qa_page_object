from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.comparison_page import ComparisonPage
from page_objects.wish_list_page import WishListPage


def test_add_to_wish_list(browser):
    # Выбор продукта из блока featured
    product_name = MainPage(browser).click_featured_product()
    # Работа на странице товара
    ProductPage(browser).add_to_wish_list()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text('login').click()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    UserPage(browser).wait_logged_in()
    # Переход и валидация вишлиста
    browser.find_element_by_css_selector('#wishlist-total').click()
    WishListPage(browser).wait_for_product_in_wish_list(product_name)


def test_add_to_cart(browser):
    # Выбор продукта из блока featured
    product_name = MainPage(browser).click_featured_product()
    # Работа на странице товара
    ProductPage(browser).add_to_cart()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Работа в корзине
    CartPage(browser).wait_for_product_in_cart(product_name)
    CartPage(browser).click_checkout()
    # Переход к логину
    CheckoutPage(browser).click_login_page_link()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Проверка отображения формы чекаута
    CheckoutPage(browser).wait_page_load()


def test_add_to_cart_from_comparison(browser):
    # Выбор продукта из блока featured
    product_name = MainPage(browser).click_featured_product()
    # Работа на странице товара
    ProductPage(browser).add_to_comparison()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("product comparison").click()
    # Работа на странице сравнения
    ComparisonPage(browser).wait_for_product_in_comparison(product_name)
    ComparisonPage(browser).click_confirm()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Работа в корзине
    CartPage(browser).wait_for_product_in_cart(product_name)
    CartPage(browser).click_checkout()
    # Переход к логину
    CheckoutPage(browser).click_login_page_link()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Проверка отображения выбора формы оплаты
    CheckoutPage(browser).wait_payment_form()
