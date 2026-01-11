from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class Header(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, '[title="Log in to your customer account"]')

    def click_sign_in(self):
        self.click(self.LOGIN_LINK)
