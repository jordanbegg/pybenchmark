import requests as r

class Sets:
    api_route = "sets"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_sets(self, exercise_id: int | None = None) -> list[dict]:
        params = {}
        url = f"{self.url}/{self.api_route}/"
        if exercise_id:
            params["exercise_id"] = exercise_id
        response = r.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve sets. Received {response.json()}")

    def get_set(self, set_id: int) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{set_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve set with id {set_id}. Received {response.json()}")

    # def create_set(self, set: str, user_id: int, date: dt.date) -> dict:
    #     response = r.post(f"{self.url}/{self.api_route}/", json={"set": set, "user_id": user_id, "date": date})
    #     if response.status_code == 200:
    #         return response.json()
    #     raise ValueError(f"Unable to create set. Received {response.json()}")

    # def delete_set(self, set_id: int) -> None:
    #     response = r.delete(f"{self.url}/{self.api_route}/{set_id}")
    #     if response.status_code != 200:
    #         raise ValueError(f"Unable to delete set with id {set_id}. Received {response.json()}")
