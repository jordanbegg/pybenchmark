import requests as r

from pybenchmark.auth import Auth, add_auth


class Permissions:
    api_route = "permissions"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_permissions(self, headers=None) -> list[dict]:
        url = f"{self.url}/{self.api_route}/"
        response = r.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve permissions. Received {response.json()}")

    @add_auth()
    def get_permission(self, permission_id: int, headers=None) -> dict:
        response = r.get(
            f"{self.url}/{self.api_route}/{permission_id}", headers=headers
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to retrieve permission with id {permission_id}. Received {response.json()}"
        )

    @add_auth()
    def create_permission(self, name: str, headers=None) -> dict:
        response = r.post(
            f"{self.url}/{self.api_route}/", json={"name": name}, headers=headers
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create permission. Received {response.json()}")

    @add_auth()
    def delete_permission(self, permission_id: int, headers=None) -> None:
        response = r.delete(
            f"{self.url}/{self.api_route}/{permission_id}", headers=headers
        )
        if response.status_code != 200:
            raise ValueError(
                f"Unable to delete permission with id {permission_id}. Received {response.json()}"
            )
