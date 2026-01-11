from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-button-action='add-to-cart']")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "button.wishlist-button-product")
    ADD_REVIEW_BUTTON = (By.CSS_SELECTOR, ".product-comments-additional-info button")
    REVIEW_FORM = (By.CSS_SELECTOR, "#post-product-comment-form")

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def click_add_to_wishlist(self):
        self.driver.find_element(*self.ADD_TO_WISHLIST_BUTTON).click()

    def click_add_review(self):
        self.driver.find_element(*self.ADD_REVIEW_BUTTON).click()

    def verify_review_form_appear(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.REVIEW_FORM))
