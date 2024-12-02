import requests as r

class WorkoutRoutines:
    api_route = "workout_routines"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_workout_routines(self, user_id: int | None = None) -> list[dict]:
        params = {}
        if user_id:
            params["user_id"] = user_id
        response = r.get(f"{self.url}/{self.api_route}/", params=params)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve workout_routines. Received {response.json()}")

    def get_workout_routine(self, workout_routine_id: int) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{workout_routine_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve workout_routine with id {workout_routine_id}. Received {response.json()}")

    def create_workout_routine(self, name: str, exercises: list, user_id: int) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"name": name, "exercises": exercises, "user_id": user_id})
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create workout_routine. Received {response.json()}")

    def delete_workout_routine(self, workout_routine_id: int) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{workout_routine_id}")
        if response.status_code != 200:
            raise ValueError(f"Unable to delete workout_routine with id {workout_routine_id}. Received {response.json()}")

    def update_workout_routines(self, workout_routine_id: int, new_name: str, new_exercises) -> dict:
        response = r.patch(
            f"{self.url}/{self.api_route}/{workout_routine_id}", json={"name": new_name, "exercises": new_exercises}
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to update workout_routine with id {workout_routine_id}. Received {response.json()}")
