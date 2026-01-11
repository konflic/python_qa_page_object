from selenium.webdriver.common.by import By

from page_objects.elements.base_element import BaseElement


class SignInModal(BaseElement):
    LOGIN_SWITCHER = (By.CSS_SELECTOR, ".wishlist-login .wishlist-modal a")

    def click_sign_in(self):
        self.click(self.LOGIN_SWITCHER)
