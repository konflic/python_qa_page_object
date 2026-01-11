from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(browser, clean_wishlist):
    # Выбор товара на главной
    feature_product = browser.find_elements(By.CSS_SELECTOR, "[data-type='popularproducts'] .product")[0]
    product_name = feature_product.find_element(By.CSS_SELECTOR, ".product-description a").text
    feature_product.click()
    # Клик по кнопке избранного
    browser.find_element(By.CSS_SELECTOR, "button.wishlist-button-product").click()
    browser.find_element(By.CSS_SELECTOR, ".modal-content a")
    browser.find_element(By.CSS_SELECTOR, ".wishlist-login .wishlist-modal a").click()
    # Авторизация
    browser.find_element(By.CSS_SELECTOR, "#field-email").send_keys("test2@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#field-password").send_keys("Mypassword123!")
    browser.find_element(By.CSS_SELECTOR, "#submit-login").click()
    # Выбор товара на главной
    feature_product = browser.find_elements(By.CSS_SELECTOR, "[data-type='popularproducts'] .product")[0]
    product_name = feature_product.find_element(By.CSS_SELECTOR, ".product-description a").text
    feature_product.click()
    # Клик по кнопке избранного
    browser.find_element(By.CSS_SELECTOR, "button.wishlist-button-product").click()
    # Выбор списка для товара
    browser.find_element(By.CSS_SELECTOR, ".wishlist-add-to .wishlist-modal li.wishlist-list-item p").click()
    # Проверка вишлиста
    browser.get(browser.url + "/module/blockwishlist/lists")
    browser.find_element(By.CSS_SELECTOR, "a.wishlist-list-item-link").click()
    # Проверка видимости товара
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".wishlist-product-title"), product_name.capitalize())
    )


def test_checkout_from_cart(browser):
    # Выбор товара на главной
    feature_product = browser.find_elements(By.CSS_SELECTOR, "[data-type='popularproducts'] .product")[0]
    product_name = feature_product.find_element(By.CSS_SELECTOR, ".product-description a").text
    feature_product.click()
    # Клик по кнопке добавления в корзину
    browser.find_element(By.CSS_SELECTOR, "[data-button-action='add-to-cart']").click()
    # Переход в корзину
    browser.find_element(By.CSS_SELECTOR, "#blockcart-modal a").click()
    # Переход в оформление заказа
    browser.find_element(By.XPATH, '//a[text()="Proceed to checkout"]').click()
    browser.find_element(By.CSS_SELECTOR, "[data-link-action='show-login-form']").click()
    # Авторизация
    browser.find_element(By.CSS_SELECTOR, "#login-form #field-email").send_keys("test2@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#login-form #field-password").send_keys("Mypassword123!")
    browser.find_element(By.CSS_SELECTOR, "#login-form [data-link-action='sign-in']").click()
    # Проверка что авторизация прошла
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delivery-address")))
    browser.find_element(By.CSS_SELECTOR, '[data-target="#cart-summary-product-list"]').click()
    # Проверка видимости товара
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.product-name"), product_name.capitalize())
    )


def test_add_product_review(browser):
    # Выбор товара на главной
    feature_product = browser.find_elements(By.CSS_SELECTOR, "[data-type='popularproducts'] .product")[0]
    product_name = feature_product.find_element(By.CSS_SELECTOR, ".product-description a").text
    feature_product.click()
    browser.find_element(By.CSS_SELECTOR, '[title="Log in to your customer account"]').click()
    # Авторизация
    browser.find_element(By.CSS_SELECTOR, "#field-email").send_keys("test2@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#field-password").send_keys("Mypassword123!")
    browser.find_element(By.CSS_SELECTOR, "#submit-login").click()
    # Клик по кнопке отзыва
    browser.find_element(By.CSS_SELECTOR, ".product-comments-additional-info button").click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#post-product-comment-form")))
    # Проверка видимости товара
    WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#post-product-comment-form p"), product_name.upper())
    )
