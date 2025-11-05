import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from conftest import username

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
WRONG_PASSWORD = '1'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
WRONG_PASSWORD_ERROR = 'Неправильно указан логин и/или пароль'

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при введенном login, но пустым password')
def test_empty_password(browser, username):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(username)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при неверном пароле')
def test_wrong_password(browser, username):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(username)
    LoginPage.type_password(WRONG_PASSWORD)
    LoginPage.type_login()
    assert LoginPage.get_error_text() == WRONG_PASSWORD_ERROR