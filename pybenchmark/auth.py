import requests as r

class Auth:
    api_route = "auth"

    def __init__(self, url: str, email: str, password: str) -> None:
        self.url = url
        self.email = email
        self.password = password
        self.token = None

    def login(self) -> str:
        payload = {"username": self.email, "password": self.password}
        url = f"{self.url}/{self.api_route}/token"
        response = r.post(url, data=payload)
        if response.status_code == 200:
            self.token = response.json().get("access_token")
        else:
            raise ValueError(f"Unable to login user. Received {response.json()}")
    
    def get_token(self):
        if not self.token:
            self.login()
        return self.token
    

def add_auth():
    def decorator(func):
        def wrapper(instance, *args, **kwargs):
            auth = instance.auth
            headers = kwargs.get("headers", {})
            headers["Authorization"] = f"Bearer {auth.get_token()}"
            kwargs["headers"] = headers
            return func(instance, *args, **kwargs)
        return wrapper
    return decorator
