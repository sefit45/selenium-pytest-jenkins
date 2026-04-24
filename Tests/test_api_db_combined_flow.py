import pytest
import allure

from api.users_api import UsersAPI
from api.payload_builder import PayloadBuilder
from api.response_validator import ResponseValidator
from utils.db_helper import DBHelper


@pytest.mark.api
@pytest.mark.db
@pytest.mark.e2e
@pytest.mark.regression
@allure.feature("API + DB Combined Flow")
@allure.story("Create user via API and validate in DB")
def test_create_user_and_validate_in_db():
    users_api = UsersAPI()
    db_helper = DBHelper()

    db_helper.create_api_users_table()

    payload = (
        PayloadBuilder()
        .with_name("Sefi")
        .with_job("QA Architect")
        .build()
    )

    response = users_api.create_user(payload)

    ResponseValidator.validate_status_code(response, 201)

    created_user = response.json()

    ResponseValidator.validate_field_exists(created_user, "id")

    user_id = created_user["id"]

    db_helper.insert_api_user(
        user_id=user_id,
        name=created_user["name"],
        job=created_user["job"]
    )

    db_user = db_helper.get_api_user_by_id(user_id)

    assert db_user is not None
    assert db_user[0] == user_id
    assert db_user[1] == "Sefi"
    assert db_user[2] == "QA Architect"