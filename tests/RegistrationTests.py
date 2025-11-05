import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
from conftest import username
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка экрана регистрации')
@allure.title('Проверка соответствия телефонного кода пользователя и кода региона при регистрации')
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_country_code