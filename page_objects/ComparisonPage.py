from selenium.webdriver.common.by import By


class ComparisonPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content")\
            .find_element(By.CSS_SELECTOR, "input[value='Add to Cart']").click()
