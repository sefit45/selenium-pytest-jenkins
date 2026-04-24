import pytest
import allure

from api.auth_api import AuthAPI


@pytest.mark.api
@pytest.mark.regression
@allure.feature("Auth API Framework")
@allure.story("Login and Token Validation")
def test_login_and_get_token():
    auth_api = AuthAPI()

    response = auth_api.login(
        email="eve.holt@reqres.in",
        password="cityslicka"
    )

    assert response.status_code == 200

    response_json = response.json()

    assert "token" in response_json
    assert response_json["token"] is not None
    assert len(response_json["token"]) > 0