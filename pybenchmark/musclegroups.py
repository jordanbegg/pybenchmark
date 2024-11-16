import requests as r

import pandas as pd


class MuscleGroups:
    api_route = "musclegroups"

    def __init__(self, url: str) -> None:
        self.url = url

    def get_musclegroups(self) -> list[dict]:
        return r.get(f"{self.url}/{self.api_route}/")

    def get_musclegroup(self, musclegroup_id: int) -> dict:
        return r.get(f"{self.url}/{self.api_route}/{musclegroup_id}")

    def create_muscle_group(self, name: str) -> dict:
        return r.post(f"{self.url}/{self.api_route}/", data={"name": name})
    
    def delete_musclegroup(self, musclegroup_id: int) -> None:
        return r.delete(f"{self.url}/{self.api_route}/{musclegroup_id}")
    
    def update_musclegroups(self, musclegroup_id: int, new_name: str) -> dict:
        return r.patch(f"{self.url}/{self.api_route}/{musclegroup_id}", data={"name": new_name})
