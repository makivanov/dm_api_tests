import pytest

from apps.api_mailhog.api.mailhog_api import MailhogApi
from apps.dm_api_account.api.account_api import AccountApi
from apps.dm_api_account.api.login_api import LoginApi
from config import BASE_API_URL, MAIL_URL


@pytest.fixture(scope="session")
def base_api_url():
    yield BASE_API_URL

@pytest.fixture(scope="session")
def mail_url():
    yield MAIL_URL

@pytest.fixture(scope="session")
def account_api(base_api_url):
    yield AccountApi(host=base_api_url)

@pytest.fixture(scope="session")
def login_api(base_api_url):
    yield LoginApi(host=base_api_url)

@pytest.fixture(scope="session")
def mailhog_api(mail_url):
    yield MailhogApi(host=mail_url)