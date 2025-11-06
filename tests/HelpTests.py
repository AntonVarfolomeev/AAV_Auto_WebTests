import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageLocators, HelpPageHelper
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite ('Проверка страницы помощи')
@allure.title ('Проверка блока "Рекламный кабинет" при скролле и открытии страницы')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)