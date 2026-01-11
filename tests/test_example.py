from page_objects.main_page import MainPage
from page_objects.elements.login_form import LoginForm
from page_objects.product_page import ProductPage
from page_objects.elements.signin_modal import SignInModal
from page_objects.elements.choose_wishlist_modal import ChooseWishlistModal
from page_objects.elements.blockcart_modal import BlockCartModal
from page_objects.elements.header import Header
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.navigation import Navigation
from page_objects.elements.product_review_modal import ProductReviewModal
from page_objects.wishlist_page import WishlistPage


def test_add_to_wish_list(browser, clean_wishlist):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).click_add_to_wishlist()
    SignInModal(browser).click_sign_in()
    LoginForm(browser).login("test2@mail.ru", "Mypassword123!", "#submit-login")
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).click_add_to_wishlist()
    ChooseWishlistModal(browser).choose_wishlist("My wishlist")
    Navigation(browser).go_to_wishlist("My wishlist")
    WishlistPage(browser).verify_product_in_wishlist(product_name.capitalize())


def test_checkout_from_cart(browser):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).click_add_to_cart()
    BlockCartModal(browser).go_to_cart()
    CartPage(browser).click_proceed_to_checkout()
    CheckoutPage(browser).switch_to_login()
    LoginForm(browser).login("test2@mail.ru", "Mypassword123!", "[data-link-action='sign-in']")
    CheckoutPage(browser).verify_delivery_form()
    CheckoutPage(browser).click_summary_products()
    CheckoutPage(browser).verify_product_in_list(product_name.capitalize())


def test_add_product_review(browser):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    Header(browser).click_sign_in()
    LoginForm(browser).login("test2@mail.ru", "Mypassword123!", "#submit-login")
    ProductPage(browser).click_add_review()
    ProductPage(browser).verify_review_form_appear()
    ProductReviewModal(browser).verify_product_name(product_name.upper())
