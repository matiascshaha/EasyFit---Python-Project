class Diet:
    def __init__(self,weight,height,age,gender):
        if gender == "M":
            self.BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
        else:
            self.BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
        self.Calorie_Calc = self.BMR * 1.55
        self.protein_proportion = self.Calorie_Calc * .4
        self.carb_proportion = self.Calorie_Calc * .4
        self.fat_proportion = self.Calorie_Calc * .2

    def print_Diet(self):
        print("Total Calories: " + str(self.Calorie_Calc))
        print("Calories of Protein: " + str(self.protein_proportion) + " (" + str(self.protein_proportion /4) + "g)")
        print("Calories of Carb: " + str(self.carb_proportion) + " (" + str(self.carb_proportion /4) + "g)")
        print("Calories of Fat: " + str(self.fat_proportion) + " (" + str(self.fat_proportion /9) + "g)")




