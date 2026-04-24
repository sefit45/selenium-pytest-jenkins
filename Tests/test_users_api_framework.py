import pytest
import allure

from api.users_api import UsersAPI
from api.payload_builder import PayloadBuilder
from api.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.regression
@allure.feature("Users API Framework")
@allure.story("Create User")
def test_create_user_with_framework():
    users_api = UsersAPI()

    payload = (
        PayloadBuilder()
        .with_name("Sefi")
        .with_job("QA Architect")
        .build()
    )

    response = users_api.create_user(payload)

    ResponseValidator.validate_status_code(response, 201)

    response_json = response.json()

    ResponseValidator.validate_field_value(
        response_json,
        "name",
        "Sefi"
    )

    ResponseValidator.validate_field_value(
        response_json,
        "job",
        "QA Architect"
    )

    ResponseValidator.validate_field_exists(
        response_json,
        "id"
    )