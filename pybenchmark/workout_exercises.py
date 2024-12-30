import requests as r

from pybenchmark.auth import Auth, add_auth


class WorkoutExercises:
    api_route = "workout_exercises"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_workout_exercises(
        self,
        exercise_id: int | None = None,
        workout_id: int | None = None,
        user_id: int | None = None,
        headers=None,
    ) -> list[dict]:
        params = {}
        url = f"{self.url}/{self.api_route}/"
        if exercise_id:
            params["exercise_id"] = exercise_id
        if workout_id:
            params["workout_id"] = workout_id
        if user_id:
            params["user_id"] = user_id
        response = r.get(url=url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to retrieve workout_exercises. Received {response.json()}"
        )

    @add_auth()
    def get_workout_exercise(self, workout_exercise_id: int, headers=None) -> dict:
        response = r.get(
            f"{self.url}/{self.api_route}/{workout_exercise_id}", headers=headers
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to retrieve workout_exercise with id {workout_exercise_id}. Received {response.json()}"
        )

    @add_auth()
    def create_workout_exercise(
        self, exercise_id: int, workout_id: int, headers=None
    ) -> dict:
        response = r.post(
            f"{self.url}/{self.api_route}/",
            json={"exercise_id": exercise_id, "workout_id": workout_id},
            headers=headers,
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to create workout_exercise. Received {response.json()}"
        )

    # def delete_workout_exercise(self, workout_exercise_id: int) -> None:
    #     response = r.delete(f"{self.url}/{self.api_route}/{workout_exercise_id}")
    #     if response.status_code != 200:
    #         raise ValueError(f"Unable to delete workout_exercise with id {workout_exercise_id}. Received {response.json()}")

    # def update_workout_exercises(self, workout_exercise_id: int, new_name: str, new_exercises) -> dict:
    #     response = r.patch(
    #         f"{self.url}/{self.api_route}/{workout_exercise_id}", json={"name": new_name, "exercises": new_exercises}
    #     )
    #     if response.status_code == 200:
    #         return response.json()
    #     raise ValueError(f"Unable to update workout_exercise with id {workout_exercise_id}. Received {response.json()}")
