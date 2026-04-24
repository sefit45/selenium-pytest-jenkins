import requests

from utils.config_manager import ConfigManager


class BaseAPI:

    def __init__(self):
        self.base_url = ConfigManager.get("base_api_url")
        api_key = ConfigManager.get("reqres_api_key")

        if not api_key:
            raise Exception("Missing REQRES_API_KEY environment variable")

        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": api_key,
            "Content-Type": "application/json"
        })

    def set_bearer_token(self, token):
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def get(self, endpoint):
        return self.session.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, payload):
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)

    def put(self, endpoint, payload):
        return self.session.put(f"{self.base_url}{endpoint}", json=payload)

    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}{endpoint}")