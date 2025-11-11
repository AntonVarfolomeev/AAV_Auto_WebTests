import pytest
from attr.validators import optional
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(command_executor="http://46.173.26.172:4444", options=options)
    yield driver
    if driver:
        driver.quit()