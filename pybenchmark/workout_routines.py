import requests as r

from pybenchmark.auth import Auth, add_auth


class WorkoutRoutines:
    api_route = "workout_routines"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_workout_routines(
        self, user_id: int | None = None, headers=None
    ) -> list[dict]:
        params = {}
        if user_id:
            params["user_id"] = user_id
        response = r.get(
            f"{self.url}/{self.api_route}/", params=params, headers=headers
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to retrieve workout_routines. Received {response.json()}"
        )

    @add_auth()
    def get_workout_routine(self, workout_routine_id: int, headers=None) -> dict:
        response = r.get(
            f"{self.url}/{self.api_route}/{workout_routine_id}", headers=headers
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to retrieve workout_routine with id {workout_routine_id}. Received {response.json()}"
        )

    @add_auth()
    def create_workout_routine(
        self, name: str, exercises: list, user_id: int, headers=None
    ) -> dict:
        response = r.post(
            f"{self.url}/{self.api_route}/",
            json={"name": name, "exercises": exercises, "user_id": user_id},
            headers=headers,
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to create workout_routine. Received {response.json()}"
        )

    @add_auth()
    def delete_workout_routine(self, workout_routine_id: int, headers=None) -> None:
        response = r.delete(
            f"{self.url}/{self.api_route}/{workout_routine_id}", headers=headers
        )
        if response.status_code != 200:
            raise ValueError(
                f"Unable to delete workout_routine with id {workout_routine_id}. Received {response.json()}"
            )

    @add_auth()
    def update_workout_routines(
        self, workout_routine_id: int, new_name: str, new_exercises, headers=None
    ) -> dict:
        response = r.patch(
            f"{self.url}/{self.api_route}/{workout_routine_id}",
            json={"name": new_name, "exercises": new_exercises},
            headers=headers,
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to update workout_routine with id {workout_routine_id}. Received {response.json()}"
        )
