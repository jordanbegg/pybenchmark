import datetime as dt
import requests as r

class Workouts:
    api_route = "workouts"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_workouts(self, workoutroutine_id: int | None = None, user_id: int | None = None) -> list[dict]:
        params = {}
        url = f"{self.url}/{self.api_route}/"
        if workoutroutine_id:
            params["workoutroutine_id"] = workoutroutine_id
        if user_id:
            params["user_id"] = user_id
        response = r.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve workouts. Received {response.json()}")

    def get_workout(self, workout_id: int) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{workout_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve workout with id {workout_id}. Received {response.json()}")
    
    def get_latest_workout(self) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/latest")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve latest workout. Received {response.json()}")

    def create_workout(self, date: dt.date, exercises: list, workoutroutine_id: int, user_id: int) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"date": date, "exercises": exercises, "workoutroutine_id": workoutroutine_id, "user_id": user_id})
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create workout. Received {response.json()}")

    def delete_workout(self, workout_id: int) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{workout_id}")
        if response.status_code != 200:
            raise ValueError(f"Unable to delete workout with id {workout_id}. Received {response.json()}")

    def update_workouts(self, workout_id: int, new_name: str, new_exercises) -> dict:
        response = r.patch(
            f"{self.url}/{self.api_route}/{workout_id}", json={"name": new_name, "exercises": new_exercises}
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to update workout with id {workout_id}. Received {response.json()}")
