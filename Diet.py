class Diet:
    def __init__(self, goal, gender):
        self.BMR
        self.Calorie_Calc

    def compute_BMR(self,weight,height,age,gender):
        if gender == "M":
            self.BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
        else:
            self.BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    def compute_Calorie_Calc(self):
        self.Calorie_Calc = self.BMR * 1.55

    def get_BMR(self):
        return self.BMR
    def get_Calories(self):
        return self.Calorie_Calc


