from selenium.webdriver.common.by import By


class ChooseWishlistModal:
    def __init__(self, driver):
        self.driver = driver

    def choose_wishlist(self, wishlist_name):
        self.driver.find_element(By.XPATH, f'//li//p[contains(text(), "{wishlist_name}")]').click()
