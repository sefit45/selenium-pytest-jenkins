class PayloadBuilder:

    def __init__(self):
        self.payload = {}

    def with_name(self, name):
        self.payload["name"] = name
        return self

    def with_job(self, job):
        self.payload["job"] = job
        return self

    def with_email(self, email):
        self.payload["email"] = email
        return self

    def with_phone(self, phone):
        self.payload["phone"] = phone
        return self

    def build(self):
        return self.payload