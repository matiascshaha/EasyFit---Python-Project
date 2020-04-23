import workout


class Person:
    def __init__(self, name, age, height, weight, goal, gender):
        self.name = name
        self.age = age;
        self.height = height
        self.weight = weight
        self.goal = goal
        self.gender = gender
        self.workout = workout(goal, gender)

