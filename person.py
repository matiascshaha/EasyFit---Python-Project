import workout
import Diet


class Person:
    def __init__(self, name, age, height, weight, goal, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.goal = goal
        self.gender = gender
        self.workout = workout.workout(goal, gender)
        self.diet = Diet.Diet(weight,height,age,gender)

