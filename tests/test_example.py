import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(browser):
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-thumb h4 a")[0]
    product_name = feature_product.text
    feature_product.click()
    browser.find_element_by_css_selector("[title='Add to Wish List']").click()
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text('login').click()
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("#form-login button").click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
    browser.find_element_by_css_selector('#wishlist-total').click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-thumb h4 a")[1]
    product_name = feature_product.text
    feature_product.click()
    browser.find_element_by_css_selector("#button-cart").click()
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_link_text("Checkout").click()
    browser.find_element_by_link_text("login page").click()
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("#form-login button[type=submit]").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "checkout-checkout")))


def test_add_to_cart_from_comparison(browser):
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-thumb h4 a")[0]
    product_name = feature_product.text
    feature_product.click()
    browser.find_element_by_css_selector("[title='Compare this Product']").click()
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("product comparison").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_css_selector("#button-confirm").click()
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_link_text("Checkout").click()
    browser.find_element_by_link_text("login page").click()
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("#form-login button[type=submit]").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "checkout-payment-method")))
