import requests as r

from pybenchmark.auth import Auth, add_auth

class Users:
    api_route = "users"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_users(self, headers=None) -> list[dict]:
        response = r.get(f"{self.url}/{self.api_route}/", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve users. Received {response.json()}")

    @add_auth()
    def get_user(self, user_id: int, headers=None) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{user_id}", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve user with id {user_id}. Received {response.json()}")

    @add_auth()
    def get_current_user(self, headers=None) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/me", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve current user. Received {response.json()}")

    def create_user(self, name: str, email: str, password: str, role_id: int | None = None, headers=None) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"name": name, "email_address": email, "password": password, "role_id": role_id}, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create user. Received {response.json()}")

    @add_auth()
    def delete_user(self, user_id: int, headers=None) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{user_id}", headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Unable to delete user with id {user_id}. Received {response.json()}")
