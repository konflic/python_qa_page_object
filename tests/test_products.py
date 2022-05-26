from selenium.webdriver.common.by import By

from page_objects.admin_page import AdminPage
from page_objects.product_page import ProductPage


def test_adding_new_product(browser):
    product = ProductPage(browser)
    product.go_to_add_new_product_form()
    product.input_product_name_field("new cool stuff")
    product.input_meta_title('new cool title')
    product.open_data_section()
    product.input_model('model 332')
    product.save()

    element = (By.XPATH, "//td[@class='text-left' and text()='new cool stuff']/preceding-sibling::td[./input]/input")
    product.delete_element(element)

def test_deleting_a_product(browser):
    product = ProductPage(browser)
    product.go_to_add_new_product_form()
    product.input_product_name_field("some stuff to delete")
    product.input_meta_title('delete title')
    product.open_data_section()
    product.input_model('model delete')
    product.save()

    element = (By.XPATH, "//td[@class='text-left' and text()='some stuff to delete']/preceding-sibling::td["
                         "./input]/input")
    product.delete_element(element)
    product._verify_element_absence(element)