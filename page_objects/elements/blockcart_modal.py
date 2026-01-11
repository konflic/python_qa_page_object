from selenium.webdriver.common.by import By

from page_objects.elements.base_element import BaseElement


class BlockCartModal(BaseElement):
    GO_TO_CART = (By.CSS_SELECTOR, "#blockcart-modal a")

    def go_to_cart(self):
        self.click(self.GO_TO_CART)
