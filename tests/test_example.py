from helpers import create_random_user
from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.comparison_page import ComparisonPage
from page_objects.wish_list_page import WishListPage
from page_objects.alert_element import AlertSuccessElement


def test_add_to_wish_list(browser, db_connection):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).add_to_wish_list()
    AlertSuccessElement(browser).login.click()
    UserPage(browser) \
        .login(*create_random_user(db_connection)) \
        .wait_logged_in() \
        .click_wish_list()
    WishListPage(browser).wait_for_product_in_wish_list(product_name)


def test_add_to_cart(browser, db_connection):
    product_name = MainPage(browser).get_featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    AlertSuccessElement(browser).shopping_cart.click()
    CartPage(browser) \
        .wait_for_product_in_cart(product_name) \
        .click_checkout()
    CheckoutPage(browser).click_login_page_link()
    UserPage(browser).login(*create_random_user(db_connection))
    CheckoutPage(browser).wait_page_load()


def test_add_to_cart_from_comparison(browser, db_connection):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).add_to_comparison()
    AlertSuccessElement(browser).comparison.click()
    ComparisonPage(browser) \
        .wait_for_product_in_comparison(product_name) \
        .click_confirm()
    AlertSuccessElement(browser).shopping_cart.click()
    CartPage(browser) \
        .wait_for_product_in_cart(product_name) \
        .click_checkout()
    CheckoutPage(browser).click_login_page_link()
    UserPage(browser).login(*create_random_user(db_connection))
    CheckoutPage(browser).wait_payment_form()
