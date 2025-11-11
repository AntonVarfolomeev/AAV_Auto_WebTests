import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from selenium.webdriver.common.by import By

class AdvertisementCabinetHelpLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')


class AdvertisementCabinetHelpHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверяем корректность страницы'):
            self.attach_screenshot()
        self.find_element(AdvertisementCabinetHelpLocators.TITLE)