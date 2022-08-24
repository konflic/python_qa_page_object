from selenium.webdriver.common.by import By


class MainPage:
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")

    def __init__(self, driver):
        self.driver = driver

    def click_featured_product(self, index):
        feature_product = self.driver.find_elements(*self.FEATURED_PRODUCT)[index]
        product_name = feature_product.find_element(*self.PRODUCT_NAME).text
        feature_product.click()
        return product_name
