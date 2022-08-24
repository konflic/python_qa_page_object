from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_featured_product(self, index):
        feature_product = self.driver.find_elements(By.CSS_SELECTOR, "#content > div.row .product-layout")[index]
        product_name = feature_product.find_element(By.CSS_SELECTOR, ".caption h4 a").text
        feature_product.click()
        return product_name
