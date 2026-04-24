class ResponseValidator:

    @staticmethod
    def validate_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, "
            f"but got {response.status_code}. "
            f"Response body: {response.text}"
        )

    @staticmethod
    def validate_field_exists(response_json, field_name):
        assert field_name in response_json, (
            f"Expected field '{field_name}' to exist in response, "
            f"but it was not found. Response: {response_json}"
        )

    @staticmethod
    def validate_field_value(response_json, field_name, expected_value):
        assert response_json[field_name] == expected_value, (
            f"Expected field '{field_name}' to be '{expected_value}', "
            f"but got '{response_json.get(field_name)}'. "
            f"Response: {response_json}"
        )