from selenium.webdriver.common.by import By


class MainPage:
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "[data-type='popularproducts'] .product")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-description a")

    def __init__(self, driver):
        self.driver = driver

    def click_featured_product(self, index=0):
        self.driver.find_elements(*self.FEATURED_PRODUCT)[index].click()

    def get_featured_product_name(self, index=0):
        feature_product = self.driver.find_elements(*self.FEATURED_PRODUCT)[index]
        return feature_product.find_element(*self.PRODUCT_NAME).text
