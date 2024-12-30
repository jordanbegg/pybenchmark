import requests as r
import datetime as dt

from pybenchmark.auth import Auth, add_auth


class Weights:
    api_route = "weights"

    def __init__(self, url: str, auth: Auth) -> None:
        self.url = url
        self.auth = auth

    @add_auth()
    def get_weights(self, user_id: int | None = None, headers=None) -> list[dict]:
        params = {}
        url = f"{self.url}/{self.api_route}/"
        if user_id:
            params["user_id"] = user_id
        response = r.get(url=url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to retrieve weights. Received {response.json()}")

    @add_auth()
    def get_weight(self, weight_id: int, headers=None) -> dict:
        response = r.get(f"{self.url}/{self.api_route}/{weight_id}", headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ValueError(
            f"Unable to retrieve weight with id {weight_id}. Received {response.json()}"
        )

    @add_auth()
    def create_weight(
        self, weight: str, user_id: int, date: dt.date, headers=None
    ) -> dict:
        response = r.post(
            f"{self.url}/{self.api_route}/",
            json={"weight": weight, "user_id": user_id, "date": date},
            headers=headers,
        )
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"Unable to create weight. Received {response.json()}")

    @add_auth()
    def delete_weight(self, weight_id: int, headers=None) -> None:
        response = r.delete(f"{self.url}/{self.api_route}/{weight_id}", headers=headers)
        if response.status_code != 200:
            raise ValueError(
                f"Unable to delete weight with id {weight_id}. Received {response.json()}"
            )
