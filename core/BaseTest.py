import pytest
from attr.validators import optional
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(command_executor="http://46.173.26.172:4444", options=options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    yield driver
    if driver:
        driver.quit()