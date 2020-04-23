class Diet:
    def __init__(self, weight, height, age, goal, gender):
        if gender == "M":
            self.BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
        else:
            self.BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
        self.goal = goal
        self.Calorie_Calc = self.BMR * 1.3
        if goal == 'C':
            self.Calorie_Calc = self.Calorie_Calc - 250
        elif goal == 'M':
            pass
        else:
            self.Calorie_Calc = self.Calorie_Calc + 250
        self.protein_proportion = self.Calorie_Calc * .4
        self.carb_proportion = self.Calorie_Calc * .4
        self.fat_proportion = self.Calorie_Calc * .2

    def print_Diet(self):
        print("TOTAL CALORIES:                      " + str(int(self.Calorie_Calc)))
        print("Calories from Protein:               " + str(int(self.protein_proportion)) + "\t\t(" + str(
            int(self.protein_proportion / 4)) + "g)")
        print("Calories from Carbohydrates:         " + str(int(self.carb_proportion)) + "\t\t(" + str(
            int(self.carb_proportion / 4)) + "g)")
        print("Calories from Fat:                   " + str(int(self.fat_proportion)) + "\t\t(" + str(
            int(self.fat_proportion / 9)) + "g)")


# class Diet:
#     def __init__(self,weight,height,age,gender):
#         if gender == "M":
#             self.BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
#         else:
#             self.BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
#         self.Calorie_Calc = self.BMR * 1.55
#         self.protein_proportion = self.Calorie_Calc * .4
#         self.carb_proportion = self.Calorie_Calc * .4
#         self.fat_proportion = self.Calorie_Calc * .2

#     def print_Diet(self):
#         print("Total Calories       :\t" + str(int(self.Calorie_Calc)))
#         print("Calories of Protein  :\t" + str(int(self.protein_proportion)) + "\t\t(" + str(int(self.protein_proportion /4)) + "g)")
#         print("Calories of Carb     :\t" + str(int(self.carb_proportion)) + "\t\t(" + str(int(self.carb_proportion /4)) + "g)")
#         print("Calories of Fat      :\t" + str(int(self.fat_proportion)) + "\t\t(" + str(int(self.fat_proportion /9)) + "g)")




