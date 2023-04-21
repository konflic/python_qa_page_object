from page_objects.MainPage import MainPage
from page_objects.UserPage import UserPage
from page_objects.ProductPage import ProductPage
from page_objects.CartPage import CartPage
from page_objects.ComparisonPage import ComparisonPage
from page_objects.elements.AlertElement import AlertElement
from test_data.users import get_user

def test_add_to_wish_list(browser):
    product_name = MainPage(browser).click_featured_product(0)
    ProductPage(browser).add_to_wish_list()
    AlertElement(browser).login.click()
    UserPage(browser)\
        .login(*get_user())\
        .open_wish_list()\
        .verify_product_item(product_name)


def test_add_to_cart(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    AlertElement(browser).cart.click()
    CartPage(browser).verify_product_item(product_name)
    CartPage(browser).click_checkout()
    UserPage(browser) \
        .login(*get_user()) \
        .verify_payment_form()


def test_add_to_cart_from_comparison(browser):
    product_name = MainPage(browser).click_featured_product(0)
    ProductPage(browser).add_to_comparison()
    AlertElement(browser).comparison.click()
    ComparisonPage(browser).verify_product_item(product_name)
    ComparisonPage(browser).add_to_cart()
    AlertElement(browser).cart.click()
    CartPage(browser).verify_product_item(product_name)
    CartPage(browser).click_checkout()
    UserPage(browser) \
        .login(*get_user()) \
        .verify_payment_form()
