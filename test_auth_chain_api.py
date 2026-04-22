import requests


def test_login_and_get_current_user():
    login_url = "https://dummyjson.com/auth/login"

    login_payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    login_headers = {
        "Content-Type": "application/json"
    }

    login_response = requests.post(login_url, json=login_payload, headers=login_headers)

    print("Login response:", login_response.json())

    assert login_response.status_code == 200
    assert "accessToken" in login_response.json()

    token = login_response.json()["accessToken"]

    user_url = "https://dummyjson.com/auth/me"

    user_headers = {
        "Authorization": f"Bearer {token}"
    }

    user_response = requests.get(user_url, headers=user_headers)

    print("User response:", user_response.json())

    assert user_response.status_code == 200
    assert user_response.json()["username"] == "emilys"
    assert "email" in user_response.json()