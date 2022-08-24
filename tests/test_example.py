import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.MainPage import MainPage
from page_objects.UserPage import UserPage
from page_objects.ProductPage import ProductPage
from page_objects.CartPage import CartPage
from page_objects.ComparisonPage import ComparisonPage


def test_add_to_wish_list(browser):
    # Выбор рекомендуемого продукта и сохранение названия
    product_name = MainPage(browser).click_featured_product(0)
    # Добавляем товар в вишлист
    ProductPage(browser).add_to_wish_list()
    # Клик по ссылке login корзины в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text('login').click()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Переходим в вишлист пользователя
    UserPage(browser).open_wish_list()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    # Выбор рекомендуемого продукта и сохранение названия
    product_name = MainPage(browser).click_featured_product(1)
    # Клик по кнопке добавления в корзину
    ProductPage(browser).add_to_cart()
    # Клик по ссылке корзины в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Клик по кнопке checkout
    CartPage(browser).click_checkout()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Проверка появления формы оплаты
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))


def test_add_to_cart_from_comparison(browser):
    # Выбор рекомендуемого продукта и сохранение названия
    product_name = MainPage(browser).click_featured_product(0)
    # Добавляем продукт в сравнение
    ProductPage(browser).add_to_comparison()
    # Клик по ссылке сравнения в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("product comparison").click()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Добавляем товар в корзину
    ComparisonPage(browser).add_to_cart()
    # Клик по ссылке корзины в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Клик по кнопке checkout
    CartPage(browser).click_checkout()
    # Авторизация
    UserPage(browser).login("test2@mail.ru", "test")
    # Проверка появления платёжной формы
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))
