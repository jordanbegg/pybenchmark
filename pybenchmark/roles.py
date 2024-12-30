import requests as r

from pybenchmark.auth import Auth, add_auth


class Roles:
    api_route = "roles"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_roles(self, headers=None) -> list[dict]:
        url = f"{self.url}/{self.api_route}/"
        response = r.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve roles. Received {response.json()}")

    @add_auth()
    def get_role(self, role_id: int, headers=None) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{role_id}", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to retrieve role with id {role_id}. Received {response.json()}"
        )

    @add_auth()
    def create_role(self, name: str, permission_ids: list[int], headers=None) -> dict:
        response = r.post(
            f"{self.url}/{self.api_route}/",
            json={"name": name, "permission_ids": permission_ids},
            headers=headers,
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create role. Received {response.json()}")

    @add_auth()
    def delete_role(self, role_id: int, headers=None) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{role_id}", headers=headers)
        if response.status_code != 200:
            raise ValueError(
                f"Unable to delete role with id {role_id}. Received {response.json()}"
            )
