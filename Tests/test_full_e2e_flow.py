import requests
import sqlite3


def test_full_e2e_flow():
    # API Login
    login_url = "https://dummyjson.com/auth/login"

    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    headers = {
        "Content-Type": "application/json"
    }

    login_response = requests.post(login_url, json=payload, headers=headers)

    print("Login Response:", login_response.json())

    assert login_response.status_code == 200

    username = login_response.json()["username"]
    email = login_response.json()["email"]

    # Database Validation
    connection = sqlite3.connect("customers.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO users (username, email)
        VALUES (?, ?)
    """, (username, email))

    connection.commit()

    cursor.execute("""
        SELECT username, email
        FROM users
        WHERE username = ?
    """, (username,))

    result = cursor.fetchone()

    print("DB Result:", result)

    assert result[0] == username
    assert result[1] == email

    connection.close()  
