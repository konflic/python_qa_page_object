from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_featured_product(self, index=0):
        self.driver.find_elements(By.CSS_SELECTOR, "[data-type='popularproducts'] .product")[index].click()

    def get_featured_product_name(self, index=0):
        feature_product = self.driver.find_elements(By.CSS_SELECTOR, "[data-type='popularproducts'] .product")[index]
        return feature_product.find_element(By.CSS_SELECTOR, ".product-description a").text
