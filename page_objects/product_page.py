import allure
from page_objects.elements.product_locators import ProductLocators
from page_objects.admin_page import AdminPage


class ProductPage(AdminPage):

    def __init__(self, browser):
        with allure.step('загружаем страницу админки'):
            self.browser, self.url = browser
            self.driver = self.browser
            self._config_logger()
            self.browser.get(self.url + '/admin')
        with allure.step('логинимся в админку'):
            AdminPage(browser).login_to_admin()
        with allure.step('открываем каталог товаров'):
            self.go_to_product_page()

    @allure.step('вводим название товара')
    def input_product_name_field(self, product_name):
        self._send_keys(ProductLocators.PRODUCT_NAME_FIELD, product_name)

    @allure.step('вводим meta title')
    def input_meta_title(self, meta_title):
        self._send_keys(ProductLocators.PRODUCT_META_TITLE, meta_title)

    @allure.step('вводим данные модели')
    def input_model(self, model):
        self._send_keys(ProductLocators.PRODUCT_MODEL, model)

    @allure.step('открываем секцию с данными')
    def open_data_section(self):
        self._click(ProductLocators.PRODUCT_DATA_BUTTON)

    allure.step('переходим в каталог')

    def go_to_product_page(self):
        self._click(ProductLocators.CATALOG_MENU)
        self._click(ProductLocators.PRODUCT_BUTTON)

    @allure.step('переходим на форму добавления товара')
    def go_to_add_new_product_form(self):
        self._click(ProductLocators.ADD_NEW)
        self._verify_element_presence(ProductLocators.PRODUCT_NAME_FIELD)

    @allure.step('сохраняем данные')
    def save(self):
        self._click(ProductLocators.SAVE)

    @allure.step('удаляем элемент')
    def delete_element(self, locator):
        self._click(locator)
        self._click(ProductLocators.DELETE)
        self.confirm_alert()

    def create_a_product(self):
        with allure.step('открываем форму создания товара'):
            self.go_to_add_new_product_form()
        with allure.step('вводим данные'):
            self.input_product_name_field("new cool stuff")
            self.input_meta_title('new cool title')
            self.open_data_section()
            self.input_model('model 332')
            self.save()

