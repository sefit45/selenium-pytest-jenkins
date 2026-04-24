import pytest
import allure

from api.auth_api import AuthAPI
from api.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("Negative API Framework")
@allure.story("Login without password should fail")
def test_login_without_password_should_fail():
    auth_api = AuthAPI()

    response = auth_api.login(
        email="eve.holt@reqres.in",
        password=""
    )

    ResponseValidator.validate_status_code(
        response,
        400
    )

    response_json = response.json()

    ResponseValidator.validate_field_exists(
        response_json,
        "error"
    )


@pytest.mark.api
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("Negative API Framework")
@allure.story("Login without email should fail")
def test_login_without_email_should_fail():
    auth_api = AuthAPI()

    response = auth_api.login(
        email="",
        password="cityslicka"
    )

    ResponseValidator.validate_status_code(
        response,
        400
    )

    response_json = response.json()

    ResponseValidator.validate_field_exists(
        response_json,
        "error"
    )


@pytest.mark.api
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("Negative API Framework")
@allure.story("Login with invalid credentials should fail")
def test_login_with_invalid_credentials_should_fail():
    auth_api = AuthAPI()

    response = auth_api.login(
        email="wrong@email.com",
        password="wrongpassword"
    )

    ResponseValidator.validate_status_code(
        response,
        400
    )

    response_json = response.json()

    ResponseValidator.validate_field_exists(
        response_json,
        "error"
    )