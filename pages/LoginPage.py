from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    QR_BUTTON = (By.XPATH, "//*[@data-l='t,get_qr']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//*[@data-l='t,restore']")
    REGISTER_BUTTON = (By.XPATH, "//*[@data-l='t,register']")
    LOGIN_TAB_BUTTON = (By.XPATH, "//*[@data-l='t,login_tab']")
    QR_CODE_TAB_BUTTON (By.XPATH, "//*[@data-l='t,qr_tab']")
    VK_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,vkc']")
    MAIL_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,mailru']")
    YANDEX_LOGIN_BUTTON = (By.XPATH, "//*[@data-l='t,yandex']")

class LoginPageHelper(BasePage):
    pass
