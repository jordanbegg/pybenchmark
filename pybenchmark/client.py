from pybenchmark.musclegroups import MuscleGroups
from pybenchmark.exercises import Exercises
from pybenchmark.workout_routines import WorkoutRoutines
from pybenchmark.workouts import Workouts

class BenchmarkClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self.musclegroups = MuscleGroups(url=url)
        self.exercises = Exercises(url=url)
        self.workout_routines = WorkoutRoutines(url=url)
        self.workouts = Workouts(url=url)
