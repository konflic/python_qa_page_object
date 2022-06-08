import allure

from page_objects.user_register_page import UserRegisterPage
from fake_user import fake_name, fake_last_name, fake_email, fake_phone, fake_password


@allure.story('test registration')
@allure.title('проверка регистрации пользователя с корректными данными')
def test_registration(browser):
    with allure.step('открываем страничку регистрации'):
        register = UserRegisterPage(browser)

    with allure.step('вводим данные'):
        register.input_name(fake_name())
        register.input_last_name(fake_last_name())
        register.input_email(fake_email())
        register.input_phone_number(fake_phone())
        register.input_password(fake_password())

    with allure.step('подтверждаем регистрацию'):
        register.confirm_privacy_policy()
        register.click_continue()
    with allure.step("проверяем пользователя"):
        register.check_registration_success()


@allure.title('тест для проверки скриншота при падении')
def test_fail(browser):
    register = UserRegisterPage(browser)
    register.input_email(fake_email())
    register.check_registration_success()
