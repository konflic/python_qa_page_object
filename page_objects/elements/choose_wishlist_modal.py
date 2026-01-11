from selenium.webdriver.common.by import By

from page_objects.elements.base_element import BaseElement


class ChooseWishlistModal(BaseElement):
    def choose_wishlist(self, wishlist_name):
        self.click((By.XPATH, f'//li//p[contains(text(), "{wishlist_name}")]'))
