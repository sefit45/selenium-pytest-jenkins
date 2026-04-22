import requests


def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print(response.json())

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["id"] == 1

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "Sefi Automation",
        "body": "Learning API testing with Python",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    print(response.json())

    assert response.status_code == 201
    assert response.json()["title"] == "Sefi Automation"
    assert response.json()["body"] == "Learning API testing with Python"
    assert response.json()["userId"] == 1