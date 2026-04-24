from api.auth_api import AuthAPI


class TokenManager:

    _token = None

    @classmethod
    def get_token(cls):
        if cls._token is None:
            auth_api = AuthAPI()

            response = auth_api.login(
                email="eve.holt@reqres.in",
                password="cityslicka"
            )

            assert response.status_code == 200

            cls._token = response.json()["token"]

        return cls._token