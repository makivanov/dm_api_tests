import pytest

from services.api_mailhog.api.mailhog_api import MailhogApi
from services.dm_api_account.api.account_api import AccountApi
from services.dm_api_account.api.login_api import LoginApi
from config import BASE_API_URL, MAIL_URL
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration

dm_api_configuration = DmApiConfiguration(host=BASE_API_URL)
mailhog_configuration = MailhogConfiguration(host=MAIL_URL)

@pytest.fixture()
def account_api():
    yield AccountApi(configuration=dm_api_configuration)

@pytest.fixture()
def login_api():
    yield LoginApi(configuration=dm_api_configuration)

@pytest.fixture()
def mailhog_api():
    yield MailhogApi(configuration=mailhog_configuration)