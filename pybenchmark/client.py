from pybenchmark.musclegroups import MuscleGroups
from pybenchmark.exercises import Exercises
from pybenchmark.workout_routines import WorkoutRoutines
from pybenchmark.workouts import Workouts
from pybenchmark.users import Users
from pybenchmark.weights import Weights
from pybenchmark.auth import Auth
from pybenchmark.sets import Sets
from pybenchmark.workout_exercises import WorkoutExercises
from pybenchmark.permissions import Permissions
from pybenchmark.roles import Roles

class BenchmarkClient:
    def __init__(self, url: str, email: str | None = None, password: str | None = None, token: str | None = None) -> None:
        self.url = url
        self.auth = Auth(url=url, email=email, password=password, token=token)
        self.musclegroups = MuscleGroups(url=url, auth=self.auth)
        self.exercises = Exercises(url=url, auth=self.auth)
        self.workout_routines = WorkoutRoutines(url=url, auth=self.auth)
        self.workouts = Workouts(url=url, auth=self.auth)
        self.users = Users(url=url, auth=self.auth)
        self.weights = Weights(url=url, auth=self.auth)
        self.sets = Sets(url=url, auth=self.auth)
        self.workout_exercises = WorkoutExercises(url=url, auth=self.auth)
        self.permissions = Permissions(url=url, auth=self.auth)
        self.roles = Roles(url=url, auth=self.auth)
