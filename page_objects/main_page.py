from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def get_featured_product_name(self, index=0):
        return self.browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a")[index].text

    def click_featured_product(self, index=0):
        self.browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a")[index].click()
