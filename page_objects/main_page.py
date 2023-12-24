from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def click_featured_product(self, index=0):
        feature_product = self.browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a")[index]
        product_name = feature_product.text
        feature_product.click()
        return product_name
