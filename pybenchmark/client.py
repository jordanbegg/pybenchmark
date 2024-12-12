from pybenchmark.musclegroups import MuscleGroups
from pybenchmark.exercises import Exercises
from pybenchmark.workout_routines import WorkoutRoutines
from pybenchmark.workouts import Workouts
from pybenchmark.users import Users
from pybenchmark.weights import Weights
from pybenchmark.auth import Auth
from pybenchmark.sets import Sets

class BenchmarkClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self.musclegroups = MuscleGroups(url=url)
        self.exercises = Exercises(url=url)
        self.workout_routines = WorkoutRoutines(url=url)
        self.workouts = Workouts(url=url)
        self.users = Users(url=url)
        self.weights = Weights(url=url)
        self.auth = Auth(url=url)
        self.sets = Sets(url=url)
