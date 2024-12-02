import requests as r

class Auth:
    api_route = "auth"

    def __init__(self, url: str) -> None:
        self.url = url

    def login_user(self, email: str, password: str) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"email_address": email, "password": password})
        if response.status_code == 200:
            return response.json()
        print(response.json())
        raise ValueError(f"Unable to login user. Received {response.json()}")