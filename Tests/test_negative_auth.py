import pytest
import requests

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.negative
def test_login_with_wrong_password():
    url = "https://dummyjson.com/auth/login"

    payload = {
        "username": "emilys",
        "password": "wrongpassword123"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

    assert response.status_code == 400
    assert "message" in response.json()
