import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    QR_BUTTON = (By.XPATH, "//*[@data-l='t,get_qr']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//*[@data-l='t,restore']")
    REGISTER_BUTTON = (By.XPATH, "//div[@class='external-oauth-login-footer']/a[@data-l='t,register']")
    LOGIN_TAB_BUTTON = (By.XPATH, "//*[@data-l='t,login_tab']")
    QR_CODE_TAB_BUTTON = (By.XPATH, "//*[@data-l='t,qr_tab']")
    VK_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,vkc']")
    MAIL_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,mailru']")
    YANDEX_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,yandex']")
    ERROR_MESSAGE = (By.XPATH, '//*[@class="input-e login_error"]')
    RETURN_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_TAB_BUTTON)
        self.find_element(LoginPageLocators.VK_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.MAIL_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_LOGIN_BUTTON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_MESSAGE).text

    @allure.step('Вводим email в поле логина')
    def type_login(self, username):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(username)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароля')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()
        self.attach_screenshot()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()