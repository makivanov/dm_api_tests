import pytest

from config import BASE_API_URL, MAIL_URL


@pytest.fixture
def base_api_url():
    return BASE_API_URL

@pytest.fixture
def mail_url():
    return MAIL_URL