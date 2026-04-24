from api.base_api import BaseAPI


class UsersAPI(BaseAPI):

    def get_users(self, page=1):
        return self.get(f"/users?page={page}")

    def get_user_by_id(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_user(self, payload):
        return self.post("/users", payload)

    def update_user(self, user_id, payload):
        return self.put(f"/users/{user_id}", payload)

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")