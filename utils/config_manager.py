import os


class ConfigManager:

    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            cls._config = {
                "base_api_url": os.getenv("BASE_API_URL", "https://reqres.in/api"),
                "reqres_api_key": os.getenv("REQRES_API_KEY"),
                "selenium_remote_url": os.getenv(
                    "SELENIUM_REMOTE_URL",
                    "http://localhost:4444/wd/hub"
                ),
                "environment": os.getenv("ENVIRONMENT", "local")
            }

        return cls._config

    @classmethod
    def get(cls, key):
        config = cls.load_config()
        return config.get(key)