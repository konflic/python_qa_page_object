from selenium.webdriver.common.by import By


class ProductLocators:
    PRODUCT_NAME_FIELD = (By.NAME, 'product_description[1][name]')
    PRODUCT_META_TITLE = (By.NAME, 'product_description[1][meta_title]')
    PRODUCT_DATA_BUTTON = (By.XPATH, "//a[contains(text(),'Data')]")
    PRODUCT_MODEL = (By.ID, 'input-model')
    PRODUCT_BUTTON = (By.XPATH, "//a[contains(text(),'Products')]")
    CATALOG_MENU = (By.ID, 'menu-catalog')
    ADD_NEW = By.CSS_SELECTOR, '[data-original-title="Add New"]'
    SAVE = By.CSS_SELECTOR, '[data-original-title="Save"]'
    DELETE = By.CSS_SELECTOR, '[data-original-title="Delete"]'
    CHECKBOX_ITEM = (By.XPATH, "//input[@type = 'checkbox']")
