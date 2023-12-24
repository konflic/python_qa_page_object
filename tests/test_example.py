import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.main_page import MainPage
from page_objects.user_page import UserPage


def test_add_to_wish_list(browser):
    # Выбор продукта из блока featured
    product_name = MainPage(browser).click_featured_product()
    # Работа на странице товара
    browser.find_element_by_css_selector("[title='Add to Wish List']").click()
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
    browser.find_element_by_css_selector("#button-cart").click()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Работа в корзине
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_link_text("Checkout").click()
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
    browser.find_element_by_css_selector("[title='Compare this Product']").click()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("product comparison").click()
    # Работа на странице сравнения
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_css_selector("#button-confirm").click()
    # Работа с алертом
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Работа в корзине
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_link_text("Checkout").click()
    # Переход к логину
    browser.find_element_by_link_text("login page").click()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Проверка отображения выбора формы оплаты
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "checkout-payment-method")))
