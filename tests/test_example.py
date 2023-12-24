from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage


def test_add_to_wish_list(browser):
    # Выбор продукта из блока featured
    product_name = MainPage(browser).click_featured_product()
    # Работа на странице товара
    ProductPage(browser).add_to_wish_list()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text('login').click()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
    # Переход и валидация вишлиста
    browser.find_element_by_css_selector('#wishlist-total').click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


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
    browser.find_element_by_link_text("login page").click()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Проверка отображения формы чекаута
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "checkout-checkout")))


def test_add_to_cart_from_comparison(browser):
    # Выбор продукта из блока featured
    product_name = MainPage(browser).click_featured_product()
    # Работа на странице товара
    ProductPage(browser).add_to_comparison()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("product comparison").click()
    # Работа на странице сравнения
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_css_selector("#button-confirm").click()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Работа в корзине
    CartPage(browser).wait_for_product_in_cart(product_name)
    CartPage(browser).click_checkout()
    # Переход к логину
    browser.find_element_by_link_text("login page").click()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Проверка отображения выбора формы оплаты
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "checkout-payment-method")))
