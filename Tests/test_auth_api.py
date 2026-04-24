import pytest
import requests

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.critical
def test_login_and_token():
    url = "https://dummyjson.com/auth/login"

    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

    assert response.status_code == 200
    assert "accessToken" in response.json()
    assert len(response.json()["accessToken"]) > 0
