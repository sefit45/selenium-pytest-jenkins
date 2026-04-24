from api.base_api import BaseAPI


class AuthAPI(BaseAPI):

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        return self.post("/login", payload)