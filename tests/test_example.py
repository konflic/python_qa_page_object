from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.main_page import MainPage
from page_objects.elements.login_form import LoginForm
from page_objects.product_page import ProductPage
from page_objects.elements.signin_modal import SignInModal
from page_objects.elements.choose_wishlist_modal import ChooseWishlistModal
from page_objects.elements.blockcart_modal import BlockCartModal
from page_objects.elements.header import Header
from page_objects.cart_page import CartPage

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
    # Проверка вишлиста
    browser.get(browser.url + "/module/blockwishlist/lists")
    browser.find_element(By.CSS_SELECTOR, "a.wishlist-list-item-link").click()
    # Проверка видимости товара
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".wishlist-product-title"), product_name.capitalize())
    )


def test_checkout_from_cart(browser):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).click_add_to_cart()
    BlockCartModal(browser).go_to_cart()
    CartPage(browser).click_proceed_to_checkout()
    browser.find_element(By.CSS_SELECTOR, "[data-link-action='show-login-form']").click()
    LoginForm(browser).login("test2@mail.ru", "Mypassword123!", "[data-link-action='sign-in']")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delivery-address")))
    browser.find_element(By.CSS_SELECTOR, '[data-target="#cart-summary-product-list"]').click()
    # Проверка видимости товара
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.product-name"), product_name.capitalize())
    )


def test_add_product_review(browser):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    Header(browser).click_sign_in()
    LoginForm(browser).login("test2@mail.ru", "Mypassword123!", "#submit-login")
    ProductPage(browser).click_add_review()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#post-product-comment-form")))
    # Проверка видимости товара
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#post-product-comment-form p"), product_name.upper())
    )
