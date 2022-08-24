import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(browser):
    # Выбор рекомендуемого продукта и сохранение названия
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[0]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    # Добавляем товар в вишлист
    browser.find_element_by_css_selector("[data-original-title='Add to Wish List']").click()
    # Клик по ссылке login корзины в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text('login').click()
    # Авторизация
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("input[value=Login]").click()
    # Переходим в вишлист пользователя
    browser.find_element_by_link_text('Wish List').click()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    # Выбор рекомендуемого продукта и сохранение названия
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[1]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    # Клик по кнопке добавления в корзину
    time.sleep(1.5) # Page loading problem
    browser.find_element_by_css_selector("#button-cart").click()
    # Клик по ссылке корзины в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Клик по кнопке checkout
    browser.find_element_by_css_selector(".buttons").find_element_by_link_text("Checkout").click()
    # Авторизация
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("input[value=Login]").click()
    # Проверка появления формы оплаты
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))


def test_add_to_cart_from_comparison(browser):
    # Выбор рекомендуемого продукта и сохранение названия
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[0]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    # Добавляем продукт в сравнение
    browser.find_element_by_css_selector("[data-original-title='Compare this Product']").click()
    # Клик по ссылке сравнения в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("product comparison").click()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Добавляем товар в корзину
    browser.find_element_by_css_selector("#content").find_element_by_css_selector("input[value='Add to Cart']").click()
    # Клик по ссылке корзины в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    # Ждём пока появится раздел с товаром
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Клик по кнопке checkout
    browser.find_element_by_css_selector(".buttons").find_element_by_link_text("Checkout").click()
    # Авторизация
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("input[value=Login]").click()
    # Проверка появления платёжной формы
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))
