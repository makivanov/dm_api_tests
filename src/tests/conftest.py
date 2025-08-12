import pytest

from endpoints.api_mailhog.api.mailhog_api import MailhogApi
from endpoints.dm_api_account.api.account_api import AccountApi
from endpoints.dm_api_account.api.login_api import LoginApi
from config import BASE_API_URL, MAIL_URL


@pytest.fixture()
def base_api_url():
    yield BASE_API_URL

@pytest.fixture()
def mail_url():
    yield MAIL_URL

@pytest.fixture()
def account_api(base_api_url):
    yield AccountApi(host=base_api_url)

@pytest.fixture()
def login_api(base_api_url):
    yield LoginApi(host=base_api_url)

@pytest.fixture()
def mailhog_api(mail_url):
    yield MailhogApi(host=mail_url)