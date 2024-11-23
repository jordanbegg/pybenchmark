import requests as r
import datetime as dt

class Weights:
    api_route = "weights"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_weights(self) -> list[dict]:
        response = r.get(f"{self.url}/{self.api_route}/")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve weights. Received {response.json()}")

    def get_weight(self, weight_id: int) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{weight_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve weight with id {weight_id}. Received {response.json()}")

    def create_weight(self, weight: str, user_id: int, date: dt.date) -> dict:
        response = r.post(f"{self.url}/{self.api_route}/", json={"weight": weight, "user_id": user_id, "date": date})
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create weight. Received {response.json()}")

    def delete_weight(self, weight_id: int) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{weight_id}")
        if response.status_code != 200:
            raise ValueError(f"Unable to delete weight with id {weight_id}. Received {response.json()}")
