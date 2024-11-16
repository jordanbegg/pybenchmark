import requests as r

class MuscleGroups:
    api_route = "musclegroups"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_musclegroups(self) -> list[dict]:
        response = r.get(f"{self.url}/{self.api_route}/")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve musclegroups. Received {response.json()}")

    def get_musclegroup(self, musclegroup_id: int) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{musclegroup_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve musclegroup with id {musclegroup_id}. Received {response.json()}")

    def create_musclegroup(self, name: str) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"name": name})
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create musclegroup. Received {response.json()}")

    def delete_musclegroup(self, musclegroup_id: int) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{musclegroup_id}")
        if response.status_code != 200:
            raise ValueError(f"Unable to delete musclegroup with id {musclegroup_id}. Received {response.json()}")

    def update_musclegroups(self, musclegroup_id: int, new_name: str) -> dict:
        response = r.patch(
            f"{self.url}/{self.api_route}/{musclegroup_id}", json={"name": new_name}
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to update musclegroup with id {musclegroup_id}. Received {response.json()}")
