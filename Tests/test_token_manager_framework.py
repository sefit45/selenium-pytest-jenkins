import pytest
import allure

from api.token_manager import TokenManager


@pytest.mark.api
@pytest.mark.regression
@allure.feature("Token Manager")
@allure.story("Get token once and reuse it")
def test_token_manager_returns_valid_token():
    token = TokenManager.get_token()

    assert token is not None
    assert isinstance(token, str)
    assert len(token) > 0