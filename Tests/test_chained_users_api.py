import pytest
import allure

from api.users_api import UsersAPI
from api.payload_builder import PayloadBuilder
from api.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.regression
@allure.feature("Chained Users API")
@allure.story("Create user and update user")
def test_create_and_update_user_flow():
    users_api = UsersAPI()

    create_payload = (
        PayloadBuilder()
        .with_name("Sefi")
        .with_job("QA Architect")
        .build()
    )

    create_response = users_api.create_user(create_payload)

    ResponseValidator.validate_status_code(create_response, 201)

    created_user = create_response.json()

    ResponseValidator.validate_field_exists(created_user, "id")

    user_id = created_user["id"]

    update_payload = (
        PayloadBuilder()
        .with_name("Sefi Updated")
        .with_job("Senior QA Architect")
        .build()
    )

    update_response = users_api.update_user(user_id, update_payload)

    ResponseValidator.validate_status_code(update_response, 200)

    updated_user = update_response.json()

    ResponseValidator.validate_field_value(
        updated_user,
        "name",
        "Sefi Updated"
    )

    ResponseValidator.validate_field_value(
        updated_user,
        "job",
        "Senior QA Architect"
    )