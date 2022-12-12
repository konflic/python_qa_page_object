import allure
from selenium.webdriver.common.by import By
from page_objects.product_page import ProductPage

@allure.story('взаимодействие с товаром')
@allure.title('тест на добавление товара')
def test_adding_new_product(browser):
    product = ProductPage(browser)
    product.create_a_product()
    with allure.step('ищем товар в таблице'):
        element = (By.XPATH, "//td[@class='text-left' and text()='new cool stuff']/preceding-sibling::td[./input]/input")

    product.delete_element(element)


def test_deleting_a_product(browser):
    with allure.step('открываем форму создания товара'):
        product = ProductPage(browser)
        product.go_to_add_new_product_form()
    with allure.step('вводим данные'):
        product.input_product_name_field("some stuff to delete")
        product.input_meta_title('delete title')
        product.open_data_section()
        product.input_model('model delete')
    with allure.step('сохраняем товар'):
        product.save()
    with allure.step('проверяем удаление'):
        element = (By.XPATH, "//td[@class='text-left' and text()='some stuff to delete']/preceding-sibling::td["
                             "./input]/input")
        product.delete_element(element)
        product._verify_element_absence(element)
