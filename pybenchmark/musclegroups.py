import requests as r
from pybenchmark.auth import Auth, add_auth

class MuscleGroups:
    api_route = "musclegroups"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_musclegroups(self, headers=None) -> list[dict]:
        response = r.get(f"{self.url}/{self.api_route}/", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve musclegroups. Received {response.json()}")

    @add_auth()
    def get_musclegroup(self, musclegroup_id: int, headers=None) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{musclegroup_id}", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve musclegroup with id {musclegroup_id}. Received {response.json()}")

    @add_auth()
    def create_musclegroup(self, name: str, headers=None) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"name": name}, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create musclegroup. Received {response.json()}")

    @add_auth()
    def delete_musclegroup(self, musclegroup_id: int, headers=None) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{musclegroup_id}", headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Unable to delete musclegroup with id {musclegroup_id}. Received {response.json()}")

    @add_auth()
    def update_musclegroups(self, musclegroup_id: int, new_name: str, headers=None) -> dict:
        response = r.patch(
            f"{self.url}/{self.api_route}/{musclegroup_id}", json={"name": new_name}, headers=headers
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to update musclegroup with id {musclegroup_id}. Received {response.json()}")
