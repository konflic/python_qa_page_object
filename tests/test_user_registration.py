from page_objects.user_register_page import UserRegisterPage
from fake_user import fake_name, fake_last_name, fake_email, fake_phone, fake_password


def test_registration(browser):
    register = UserRegisterPage(browser)
    register.input_name(fake_name())
    register.input_last_name(fake_last_name())
    register.input_email(fake_email())
    register.input_phone_number(fake_phone())
    register.input_password(fake_password())
    register.confirm_privacy_policy()
    register.click_continue()
    register.check_registration_success()




