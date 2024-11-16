import requests as r

class Exercises:
    api_route = "exercises"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_exercises(self) -> list[dict]:
        response = r.get(f"{self.url}/{self.api_route}/")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve exercises. Received {response.json()}")

    def get_exercise(self, exercise_id: int) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{exercise_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve exercise with id {exercise_id}. Received {response.json()}")

    def create_exercise(self, name: str, musclegroup_ids: list[str]) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"name": name, "musclegroup_ids": musclegroup_ids})
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create exercise. Received {response.json()}")

    def delete_exercise(self, exercise_id: int) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{exercise_id}")
        if response.status_code != 200:
            raise ValueError(f"Unable to delete exercise with id {exercise_id}. Received {response.json()}")

    def update_exercises(self, exercise_id: int, new_name: str, new_musclegroup_ids) -> dict:
        response = r.patch(
            f"{self.url}/{self.api_route}/{exercise_id}", json={"name": new_name, "musclegroup_ids": new_musclegroup_ids}
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to update exercise with id {exercise_id}. Received {response.json()}")
