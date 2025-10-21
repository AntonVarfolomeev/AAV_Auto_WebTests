from pages.BasePage import BasePage
from faker import Faker
import pytest

@pytest.fixture(scope="session")
def username():
    faker = Faker()
    login = faker.email()
    return login
