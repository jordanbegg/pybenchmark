import requests as r
from pybenchmark.auth import Auth, add_auth

class Exercises:
    api_route = "exercises"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_exercises(self, headers=None) -> list[dict]:
        response = r.get(f"{self.url}/{self.api_route}/", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve exercises. Received {response.json()}")

    @add_auth()
    def get_exercise(self, exercise_id: int, headers=None) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{exercise_id}", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve exercise with id {exercise_id}. Received {response.json()}")

    @add_auth()
    def create_exercise(self, name: str, musclegroup_ids: list[str], headers=None) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"name": name, "musclegroup_ids": musclegroup_ids}, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create exercise. Received {response.json()}")

    @add_auth()
    def delete_exercise(self, exercise_id: int, headers=None) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{exercise_id}", headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Unable to delete exercise with id {exercise_id}. Received {response.json()}")

    @add_auth()
    def update_exercises(self, exercise_id: int, new_name: str, new_musclegroup_ids, headers=None) -> dict:
        response = r.patch(
            f"{self.url}/{self.api_route}/{exercise_id}", json={"name": new_name, "musclegroup_ids": new_musclegroup_ids}, headers=headers
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to update exercise with id {exercise_id}. Received {response.json()}")
