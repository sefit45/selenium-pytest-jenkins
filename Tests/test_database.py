import pytest
import sqlite3

@pytest.mark.db
@pytest.mark.regression
def test_database_validation():
    connection = sqlite3.connect("customers.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO customers (name, email)
        VALUES ('Sefi', 'sefi@test.com')
    """)

    connection.commit()

    cursor.execute("""
        SELECT name, email
        FROM customers
        WHERE name = 'Sefi'
    """)

    result = cursor.fetchone()

    print(result)

    assert result[0] == "Sefi"
    assert result[1] == "sefi@test.com"

    connection.close()
