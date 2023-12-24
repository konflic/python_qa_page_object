from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class UserPage(BasePage):
    LOGIN_INPUT = By.CSS_SELECTOR, "#input-email"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    SUBMIT_LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login button"
    LOGOUT_LINK = By.LINK_TEXT, "Logout"
    USER_MENU = By.CSS_SELECTOR, "#column-right"
    WISH_LIST_LINK = By.LINK_TEXT, "Wish List"

    def login(self, username, password):
        self.get_element(self.LOGIN_INPUT).send_keys(username)
        self.get_element(self.PASSWORD_INPUT).send_keys(password)
        self.get_element(self.SUBMIT_LOGIN_BUTTON).click()

    def wait_logged_in(self):
        self.get_element(self.LOGOUT_LINK)

    def click_wish_list(self):
        self.get_element(self.USER_MENU).find_element(*self.WISH_LIST_LINK).click()
