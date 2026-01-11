from selenium.webdriver.common.by import By


class Navigation:
    def __init__(self, driver):
        self.driver = driver

    def go_to_wishlist(self, wishlist_name):
        self.driver.get(self.driver.url + "/module/blockwishlist/lists")
        self.driver.find_element(By.XPATH, f'//a//p[contains(text(), "{wishlist_name}")]').click()
