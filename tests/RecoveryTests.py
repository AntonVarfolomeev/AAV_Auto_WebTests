import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelperHelper
from conftest import username

BASE_URL = 'https://ok.ru/'
PASSWORD_TEXT = '1'

@allure.suite('Проверка экрана восстановления данных')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_multiple_fails(browser, username):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(username)

    for i in range (3):
        LoginPage.type_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelperHelper(browser)

