from pages.BasePage import BasePageHelper
from faker import Faker
import pytest

@pytest.fixture(scope="session")
def username():
    faker = Faker()
    login = faker.email()
    return login
