import requests as r

class Users:
    api_route = "users"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_users(self) -> list[dict]:
        response = r.get(f"{self.url}/{self.api_route}/")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve users. Received {response.json()}")

    def get_user(self, user_id: int) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve user with id {user_id}. Received {response.json()}")

    def create_user(self, name: str, email: str) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"name": name, "email_address": email})
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create user. Received {response.json()}")

    def delete_user(self, user_id: int) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{user_id}")
        if response.status_code != 200:
            raise ValueError(f"Unable to delete user with id {user_id}. Received {response.json()}")
