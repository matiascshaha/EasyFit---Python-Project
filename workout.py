class Workout:
    def __init__(self, goal, gender):
        self.goal = goal
        self.gender = gender

    def printWorkout(self):
        if self.gender == 'M' and self.goal == 'C':
            sunday = "CARDIO"
            monday = "CHEST/TRICEPS\nBench Press\t12 x 10 x 8\nIncline Dumbbell Press\t12 x 10 x 8\nCable Flys\t14 x " \
                     "12 x 10\nDips\t3 x AMRAP\nTricep Pulldown\t15 x 15 x 15 "
            tuesday = "BACK/BICEPS\nPull-Ups\t3 x AMRAP\nCable Row\t14 x 12 x 10\nLat Pullover\t20 x 15 x 10\nBarbell " \
                      "Curl\t16 x 14 x 12\nPreacher Curl\t16 x 14 x 12\nDumbbell Curl\t16 x 14 x 12 "
            wednesday = "SHOULDERS/TRAPS\nShoulder Press\t12 x 10 x 8\nArnold Press\t14 x 12 x 10\nLateral Raise\t16 " \
                        "x 14 x 12\nReverse Pec Dec\t16 x 14 x 12\nBarbell Shrugs\t14 x 12 x 10 "
            thursday = "LEGS\nSquats\n12 x 10 x 8 x 6\nQuad Extensions\t14 x 12 x 10\nHamstring Curls\t14 x 12 x " \
                       "10\nCalf Raises\t20 x 18 x 16 x 14 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'M' and self.goal == 'M':
            sunday = "REST"
            monday = "CHEST/TRICEPS\nBench Press\t12 x 10 x 8\nIncline Dumbbell Press\t12 x 10 x 8\nCable Flys\t14 x " \
                     "12 x 10\nDips\t3 x AMRAP\nTricep Pulldown\t15 x 15 x 15 "
            tuesday = "BACK/BICEPS\nPull-Ups\t3 x AMRAP\nCable Row\t14 x 12 x 10\nLat Pullover\t20 x 15 x 10\nBarbell " \
                      "Curl\t16 x 14 x 12\nPreacher Curl\t16 x 14 x 12\nDumbbell Curl\t16 x 14 x 12 "
            wednesday = "SHOULDERS/TRAPS\nShoulder Press\t12 x 10 x 8\nArnold Press\t14 x 12 x 10\nLateral Raise\t16 " \
                        "x 14 x 12\nReverse Pec Dec\t16 x 14 x 12\nBarbell Shrugs\t14 x 12 x 10 "
            thursday = "LEGS\nSquats\n12 x 10 x 8 x 6\nQuad Extensions\t14 x 12 x 10\nHamstring Curls\t14 x 12 x " \
                       "10\nCalf Raises\t20 x 18 x 16 x 14 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'M' and self.goal == 'B':
            sunday = "DEADLIFT\nDeadlifts\t5 x 5 x 5 x 5 x 5"
            monday = "CHEST/TRICEPS\nBench Press\t10 x 8 x 6\nIncline Dumbbell Press\t10 x 8 x 6\nCable Flys\t12 x 10 " \
                     "x 8\nDips\t3 x AMRAP\nTricep Pulldown\t15 x 15 x 15 "
            tuesday = "BACK/BICEPS\nPull-Ups\t3 x AMRAP\nCable Row\t12 x 10 x 8\nLat Pullover\t16 x 14 x 12\nBarbell " \
                      "Curl\t16 x 14 x 12\nPreacher Curl\t16 x 14 x 12\nDumbbell Curl\t16 x 14 x 12 "
            wednesday = "SHOULDERS/TRAPS\nShoulder Press\t10 x 8 x 6\nArnold Press\t12 x 10 x 8\nLateral Raise\t14 x " \
                        "12 x 10\nReverse Pec Dec\t14 x 12 x 10\nBarbell Shrugs\t12 x 10 x 8 x 6 "
            thursday = "LEGS\nSquats\n10 x 8 x 6 x 4\nQuad Extensions\t14 x 12 x 10\nHamstring Curls\t14 x 12 x " \
                       "10\nCalf Raises\t18 x 16 x 14 x 12 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'F' and self.goal == 'C':
            sunday = "CARDIO"
            monday = "LEGS/GLUTES\nSquats\t16 x 14 x 12\nHip Thrusts\t20 x 15 x 10\nRomanian Deadlift\t16 x 14 x " \
                     "12\nQuad Extensions\t18 x 16 x 14\nCalf Raises\t20 x 20 x 20 "
            tuesday = "UPPER BODY\n(Assisted) Pull-Ups\t3 x AMRAP\nDumbbell Press\t18 x 16 x 14\nDumbbell Shoulder " \
                      "Press\t18 x 16 x 14\nPec Dec\t18 x 16 x 14\nReverse Pec Dec\t18 x 16 x 14 "
            wednesday = "ARMS/ABS\nBarbell Curls\t18 x 16 x 14\tSkullcrushers\t18 x 16 x 14\nCable Curls\t18 x 16 x " \
                        "14\nTricep Pulldown\t18 x 16 x 14\n(Assisted) Pull-Ups and Dips\t3 x AMRAP "
            thursday = "LEGS/GLUTES\nSquats\t16 x 14 x 12\nHip Thrusts\t20 x 15 x 10\nRomanian Deadlift\t16 x 14 x " \
                       "12\nQuad Extensions\t18 x 16 x 14\nCalf Raises\t20 x 20 x 20 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'F' and self.goal == 'M':
            sunday = "REST"
            monday = "LEGS/GLUTES\nSquats\t16 x 14 x 12\nHip Thrusts\t20 x 15 x 10\nRomanian Deadlift\t16 x 14 x " \
                     "12\nQuad Extensions\t18 x 16 x 14\nCalf Raises\t20 x 20 x 20 "
            tuesday = "UPPER BODY\n(Assisted) Pull-Ups\t3 x AMRAP\nDumbbell Press\t18 x 16 x 14\nDumbbell Shoulder " \
                      "Press\t18 x 16 x 14\nPec Dec\t18 x 16 x 14\nReverse Pec Dec\t18 x 16 x 14 "
            wednesday = "ARMS/ABS\nBarbell Curls\t18 x 16 x 14\tSkullcrushers\t18 x 16 x 14\nCable Curls\t18 x 16 x " \
                        "14\nTricep Pulldown\t18 x 16 x 14\n(Assisted) Pull-Ups and Dips\t3 x AMRAP "
            thursday = "LEGS/GLUTES\nSquats\t16 x 14 x 12\nHip Thrusts\t20 x 15 x 10\nRomanian Deadlift\t16 x 14 x " \
                       "12\nQuad Extensions\t18 x 16 x 14\nCalf Raises\t20 x 20 x 20 "
            friday = "REST"
            saturday = "REST"
        else:
            sunday = "REST"
            monday = "LEGS/GLUTES\nSquats\t12 x 10 x 8\nHip Thrusts\t16 x 14 x 12\nRomanian Deadlift\t12 x 10 x " \
                     "8\nQuad Extensions\t14 x 12 x 10\nCalf Raises\t14 x 12 x 10 "
            tuesday = "UPPER BODY\n(Assisted) Pull-Ups\t3 x AMRAP\nDumbbell Press\t14 x 12 x 10\nDumbbell Shoulder " \
                      "Press\t14 x 12 x 10\nPec Dec\t14 x 12 x 10\nReverse Pec Dec\t14 x 12 x 10 "
            wednesday = "ARMS/ABS\nBarbell Curls\t16 x 14 x 12\tSkullcrushers\t16 x 14 x 12\nCable Curls\t16 x 14 x " \
                        "12\nTricep Pulldown\t16 x 14 x 12\n(Assisted) Pull-Ups and Dips\t3 x AMRAP "
            thursday = "LEGS/GLUTES\nSquats\t12 x 10 x 8\nHip Thrusts\t16 x 14 x 12\nRomanian Deadlift\t12 x 10 x " \
                       "8\nQuad Extensions\t14 x 12 x 10\nCalf Raises\t14 x 12 x 10 "
            friday = "REST"
            saturday = "REST"

        plan = "SUNDAY:\n" + sunday + "\n" + "MONDAY:\n" + monday + "\n" + "TUESDAY:\n" + tuesday + "\n" + \
               "WEDNESDAY:\n" + wednesday + "\n" + "THURSDAY:\n" + thursday + "\n" + "FRIDAY:\n" + friday + "\n" + \
               "SATURDAY:\n" + saturday + "\n"

        print(plan)


