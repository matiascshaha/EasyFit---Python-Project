class workout:
    def __init__(self, goal, gender):
        self.goal = goal
        self.gender = gender

    def printWorkout(self):
        if self.gender == 'M' and self.goal == 'C':
            sunday = "CARDIO"
            monday = "CHEST/TRICEPS\n" \
                     "\tBench Press                         12 x 10 x 8\n" \
                     "\tIncline Dumbbell Press              12 x 10 x 8\n" \
                     "\tCable Flys                          14 x 12 x 10\n" \
                     "\tDips                                3 x AMRAP\n" \
                     "\tTricep Pulldown                     15 x 15 x 15"
            tuesday = "BACK/BICEPS\n" \
                      "\tPull-Ups                           3 x AMRAP\n" \
                      "\tCable Row                          14 x 12 x 10\n" \
                      "\tLat Pullover                       20 x 15 x 10\n" \
                      "\tBarbell Curl                       16 x 14 x 12\n" \
                      "\tPreacher Curl                      16 x 14 x 12\n" \
                      "\tDumbbell Curl                      16 x 14 x 12"
            wednesday = "SHOULDERS/TRAPS\n" \
                        "\tShoulder Press                   12 x 10 x 8\n" \
                        "\tArnold Press                     14 x 12 x 10\n" \
                        "\tLateral Raise                    16 x 14 x 12\n" \
                        "\tReverse Pec Dec                  16 x 14 x 12\n" \
                        "\tBarbell Shrugs                   14 x 12 x 10"
            thursday = "LEGS\n" \
                       "\tSquats                            12 x 10 x 8 x 6\n" \
                       "\tQuad Extensions                   14 x 12 x 10\n" \
                       "\tHamstring Curls                   14 x 12 x 10\n" \
                       "\tCalf Raises                       20 x 18 x 16 x 14 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'M' and self.goal == 'M':
            sunday = "REST"
            monday = "CHEST/TRICEPS\n" \
                     "\tBench Press                         12 x 10 x 8\n" \
                     "\tIncline Dumbbell Press              12 x 10 x 8\n" \
                     "\tCable Flys                          14 x 12 x 10\n" \
                     "\tDips                                3 x AMRAP\n" \
                     "\tTricep Pulldown                     15 x 15 x 15"
            tuesday = "BACK/BICEPS\n" \
                      "\tPull-Ups                           3 x AMRAP\n" \
                      "\tCable Row                          14 x 12 x 10\n" \
                      "\tLat Pullover                       20 x 15 x 10\n" \
                      "\tBarbell Curl                       16 x 14 x 12\n" \
                      "\tPreacher Curl                      16 x 14 x 12\n" \
                      "\tDumbbell Curl                      16 x 14 x 12"
            wednesday = "SHOULDERS/TRAPS\n" \
                        "\tShoulder Press                   12 x 10 x 8\n" \
                        "\tArnold Press                     14 x 12 x 10\n" \
                        "\tLateral Raise                    16 x 14 x 12\n" \
                        "\tReverse Pec Dec                  16 x 14 x 12\n" \
                        "\tBarbell Shrugs                   14 x 12 x 10"
            thursday = "LEGS\n" \
                       "\tSquats                            12 x 10 x 8 x 6\n" \
                       "\tQuad Extensions                   14 x 12 x 10\n" \
                       "\tHamstring Curls                   14 x 12 x 10\n" \
                       "\tCalf Raises                       20 x 18 x 16 x 14 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'M' and self.goal == 'B':
            sunday = "DEADLIFT\n" \
                     "\tDeadlifts                           5 x 5 x 5 x 5 x 5"
            monday = "CHEST/TRICEPS\n" \
                     "\tBench Press                         10 x 8 x 6\n" \
                     "\tIncline Dumbbell Press              10 x 8 x 6\n" \
                     "\tCable Flys                          12 x 10 x 8\n" \
                     "\tDips                                3 x AMRAP\n" \
                     "\tTricep Pulldown                     15 x 15 x 15"
            tuesday = "BACK/BICEPS\n" \
                      "\tPull-Ups                           3 x AMRAP\n" \
                      "\tCable Row                          12 x 10 x 8\n" \
                      "\tLat Pullover                       16 x 14 x 12\n" \
                      "\tBarbell Curl                       16 x 14 x 12\n" \
                      "\tPreacher Curl                      16 x 14 x 12\n" \
                      "\tDumbbell Curl                      16 x 14 x 12 "
            wednesday = "SHOULDERS/TRAPS\n" \
                        "\tShoulder Press                   10 x 8 x 6\n" \
                        "\tArnold Press                     12 x 10 x 8\n" \
                        "\tLateral Raise                    14 x 12 x 10\n" \
                        "\tReverse Pec Dec                  14 x 12 x 10\n" \
                        "\tBarbell Shrugs                   12 x 10 x 8 x 6 "
            thursday = "LEGS\n" \
                       "\tSquats                            10 x 8 x 6 x 4\n" \
                       "\tQuad Extensions                   14 x 12 x 10\n" \
                       "\tHamstring Curls                   14 x 12 x 10\n" \
                       "\tCalf Raises                       18 x 16 x 14 x 12 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'F' and self.goal == 'C':
            sunday = "CARDIO"
            monday = "LEGS/GLUTES\n" \
                     "\tSquats                              16 x 14 x 12\n" \
                     "\tHip Thrusts                         20 x 15 x 10\n" \
                     "\tRomanian Deadlifts                  16 x 14 x 12\n" \
                     "\tQuad Extensions                     18 x 16 x 14\n" \
                     "\tCalf Raises                         20 x 20 x 20 "
            tuesday = "UPPER BODY\n" \
                      "\t(Assisted) Pull-Ups                3 x AMRAP\n" \
                      "\tDumbbell Press                     18 x 16 x 14\n" \
                      "\tDumbbell Shoulder Press            18 x 16 x 14\n" \
                      "\tPec Dec                            18 x 16 x 14\n" \
                      "\tReverse Pec Dec                    18 x 16 x 14 "
            wednesday = "ARMS/ABS\n" \
                        "\tBarbell Curls                    18 x 16 x 14\n" \
                        "\tSkullcrushers                    18 x 16 x 14\n" \
                        "\tCable Curls                      18 x 16 x 14\n" \
                        "\tTricep Pulldown                  18 x 16 x 14\n" \
                        "\t(Assisted) Pull-Ups and Dips     3 x AMRAP "
            thursday = "LEGS/GLUTES\n" \
                       "\tSquats                            16 x 14 x 12\n" \
                       "\tHip Thrusts                       20 x 15 x 10\n" \
                       "\tRomanian Deadlifts                16 x 14 x 12\n" \
                       "\tQuad Extensions                   18 x 16 x 14\n" \
                       "\tCalf Raises                       20 x 20 x 20 "
            friday = "REST"
            saturday = "REST"
        elif self.gender == 'F' and self.goal == 'M':
            sunday = "REST"
            monday = "LEGS/GLUTES\n" \
                     "\tSquats                              16 x 14 x 12\n" \
                     "\tHip Thrusts                         20 x 15 x 10\n" \
                     "\tRomanian Deadlifts                  16 x 14 x 12\n" \
                     "\tQuad Extensions                     18 x 16 x 14\n" \
                     "\tCalf Raises                         20 x 20 x 20 "
            tuesday = "UPPER BODY\n" \
                      "\t(Assisted) Pull-Ups                3 x AMRAP\n" \
                      "\tDumbbell Press                     18 x 16 x 14\n" \
                      "\tDumbbell Shoulder Press            18 x 16 x 14\n" \
                      "\tPec Dec                            18 x 16 x 14\n" \
                      "\tReverse Pec Dec                    18 x 16 x 14 "
            wednesday = "ARMS/ABS\n" \
                        "\tBarbell Curls                    18 x 16 x 14\n" \
                        "\tSkullcrushers                    18 x 16 x 14\n" \
                        "\tCable Curls                      18 x 16 x 14\n" \
                        "\tTricep Pulldown                  18 x 16 x 14\n" \
                        "\t(Assisted) Pull-Ups and Dips     3 x AMRAP "
            thursday = "LEGS/GLUTES\n" \
                       "\tSquats                            16 x 14 x 12\n" \
                       "\tHip Thrusts                       20 x 15 x 10\n" \
                       "\tRomanian Deadlift                 16 x 14 x 12\n" \
                       "\tQuad Extensions                   18 x 16 x 14\n" \
                       "\tCalf Raises                       20 x 20 x 20 "
            friday = "REST"
            saturday = "REST"
        else:
            sunday = "REST"
            monday = "LEGS/GLUTES\n" \
                     "\tSquats                              12 x 10 x 8\n" \
                     "\tHip Thrusts                         16 x 14 x 12\n" \
                     "\tRomanian Deadlift                   12 x 10 x 8\n" \
                     "\tQuad Extensions                     14 x 12 x 10\n" \
                     "\tCalf Raises                         14 x 12 x 10 "
            tuesday = "UPPER BODY\n" \
                      "\t(Assisted) Pull-Ups                3 x AMRAP\n" \
                      "\tDumbbell Press                     14 x 12 x 10\n" \
                      "\tDumbbell Shoulder Press            14 x 12 x 10\n" \
                      "\tPec Dec                            14 x 12 x 10\n" \
                      "\tReverse Pec Dec                    14 x 12 x 10 "
            wednesday = "ARMS/ABS\n" \
                        "\tBarbell Curls                    16 x 14 x 12\n" \
                        "\tSkullcrushers                    16 x 14 x 12\n" \
                        "\tCable Curls                      16 x 14 x 12\n" \
                        "\tTricep Pulldown                  16 x 14 x 12\n" \
                        "\t(Assisted) Pull-Ups and Dips     3 x AMRAP "
            thursday = "LEGS/GLUTES\n" \
                       "\tSquats                            12 x 10 x 8\n" \
                       "\tHip Thrusts                       16 x 14 x 12\n" \
                       "\tRomanian Deadlifts                12 x 10 x 8\n" \
                       "\tQuad Extensions                   14 x 12 x 10\n" \
                       "\tCalf Raises                       14 x 12 x 10 "
            friday = "REST"
            saturday = "REST"

        plan = "SUNDAY: " + sunday + "\n\n" + "MONDAY: " \
               + monday + "\n\n" + "TUESDAY: " + tuesday + "\n\n" + "WEDNESDAY: " + wednesday + "\n\n" + \
               "THURSDAY: " + thursday + "\n\n" + "FRIDAY: " + friday + "\n\n" + "SATURDAY: " + saturday + \
               "\n\n"

        return plan

# class workout:
#     def __init__(self, goal, gender):
#         self.goal = goal
#         self.gender = gender

#     def printWorkout(self):
#         if self.gender == 'M' and self.goal == 'C':
#             sunday = "CARDIO"
#             monday = "CHEST/TRICEPS\n" \
#                      "\tBench Press                         12 x 10 x 8\n" \
#                      "\tIncline Dumbbell Press              12 x 10 x 8\n" \
#                      "\tCable Flys                          14 x 12 x 10\n" \
#                      "\tDips                                3 x AMRAP\n" \
#                      "\tTricep Pulldown                     15 x 15 x 15"
#             tuesday = "BACK/BICEPS\n" \
#                       "\tPull-Ups                           3 x AMRAP\n" \
#                       "\tCable Row                          14 x 12 x 10\n" \
#                       "\tLat Pullover                       20 x 15 x 10\n" \
#                       "\tBarbell Curl                       16 x 14 x 12\n" \
#                       "\tPreacher Curl                      16 x 14 x 12\n" \
#                       "\tDumbbell Curl                      16 x 14 x 12"
#             wednesday = "SHOULDERS/TRAPS\n" \
#                         "\tShoulder Press                   12 x 10 x 8\n" \
#                         "\tArnold Press                     14 x 12 x 10\n" \
#                         "\tLateral Raise                    16 x 14 x 12\n" \
#                         "\tReverse Pec Dec                  16 x 14 x 12\n" \
#                         "\tBarbell Shrugs                   14 x 12 x 10"
#             thursday = "LEGS\n" \
#                        "\tSquats                            12 x 10 x 8 x 6\n" \
#                        "\tQuad Extensions                   14 x 12 x 10\n" \
#                        "\tHamstring Curls                   14 x 12 x 10\n" \
#                        "\tCalf Raises                       20 x 18 x 16 x 14 "
#             friday = "REST"
#             saturday = "REST"
#         elif self.gender == 'M' and self.goal == 'M':
#             sunday = "REST"
#             monday = "CHEST/TRICEPS\n" \
#                      "\tBench Press                         12 x 10 x 8\n" \
#                      "\tIncline Dumbbell Press              12 x 10 x 8\n" \
#                      "\tCable Flys                          14 x 12 x 10\n" \
#                      "\tDips                                3 x AMRAP\n" \
#                      "\tTricep Pulldown                     15 x 15 x 15"
#             tuesday = "BACK/BICEPS\n" \
#                       "\tPull-Ups                           3 x AMRAP\n" \
#                       "\tCable Row                          14 x 12 x 10\n" \
#                       "\tLat Pullover                       20 x 15 x 10\n" \
#                       "\tBarbell Curl                       16 x 14 x 12\n" \
#                       "\tPreacher Curl                      16 x 14 x 12\n" \
#                       "\tDumbbell Curl                      16 x 14 x 12"
#             wednesday = "SHOULDERS/TRAPS\n" \
#                         "\tShoulder Press                   12 x 10 x 8\n" \
#                         "\tArnold Press                     14 x 12 x 10\n" \
#                         "\tLateral Raise                    16 x 14 x 12\n" \
#                         "\tReverse Pec Dec                  16 x 14 x 12\n" \
#                         "\tBarbell Shrugs                   14 x 12 x 10"
#             thursday = "LEGS\n" \
#                        "\tSquats                            12 x 10 x 8 x 6\n" \
#                        "\tQuad Extensions                   14 x 12 x 10\n" \
#                        "\tHamstring Curls                   14 x 12 x 10\n" \
#                        "\tCalf Raises                       20 x 18 x 16 x 14 "
#             friday = "REST"
#             saturday = "REST"
#         elif self.gender == 'M' and self.goal == 'B':
#             sunday = "DEADLIFT\n" \
#                      "\tDeadlifts                           5 x 5 x 5 x 5 x 5"
#             monday = "CHEST/TRICEPS\n" \
#                      "\tBench Press                         10 x 8 x 6\n" \
#                      "\tIncline Dumbbell Press              10 x 8 x 6\n" \
#                      "\tCable Flys                          12 x 10 x 8\n" \
#                      "\tDips                                3 x AMRAP\n" \
#                      "\tTricep Pulldown                     15 x 15 x 15"
#             tuesday = "BACK/BICEPS\n" \
#                       "\tPull-Ups                           3 x AMRAP\n" \
#                       "\tCable Row                          12 x 10 x 8\n" \
#                       "\tLat Pullover                       16 x 14 x 12\n" \
#                       "\tBarbell Curl                       16 x 14 x 12\n" \
#                       "\tPreacher Curl                      16 x 14 x 12\n" \
#                       "\tDumbbell Curl                      16 x 14 x 12 "
#             wednesday = "SHOULDERS/TRAPS\n" \
#                         "\tShoulder Press                   10 x 8 x 6\n" \
#                         "\tArnold Press                     12 x 10 x 8\n" \
#                         "\tLateral Raise                    14 x 12 x 10\n" \
#                         "\tReverse Pec Dec                  14 x 12 x 10\n" \
#                         "\tBarbell Shrugs                   12 x 10 x 8 x 6 "
#             thursday = "LEGS\n" \
#                        "\tSquats                            10 x 8 x 6 x 4\n" \
#                        "\tQuad Extensions                   14 x 12 x 10\n" \
#                        "\tHamstring Curls                   14 x 12 x 10\n" \
#                        "\tCalf Raises                       18 x 16 x 14 x 12 "
#             friday = "REST"
#             saturday = "REST"
#         elif self.gender == 'F' and self.goal == 'C':
#             sunday = "CARDIO"
#             monday = "LEGS/GLUTES\n" \
#                      "\tSquats                              16 x 14 x 12\n" \
#                      "\tHip Thrusts                         20 x 15 x 10\n" \
#                      "\tRomanian Deadlifts                  16 x 14 x 12\n" \
#                      "\tQuad Extensions                     18 x 16 x 14\n" \
#                      "\tCalf Raises                         20 x 20 x 20 "
#             tuesday = "UPPER BODY\n" \
#                       "\t(Assisted) Pull-Ups                3 x AMRAP\n" \
#                       "\tDumbbell Press                     18 x 16 x 14\n" \
#                       "\tDumbbell Shoulder Press            18 x 16 x 14\n" \
#                       "\tPec Dec                            18 x 16 x 14\n" \
#                       "\tReverse Pec Dec                    18 x 16 x 14 "
#             wednesday = "ARMS/ABS\n" \
#                         "\tBarbell Curls                    18 x 16 x 14\n" \
#                         "\tSkullcrushers                    18 x 16 x 14\n" \
#                         "\tCable Curls                      18 x 16 x 14\n" \
#                         "\tTricep Pulldown                  18 x 16 x 14\n" \
#                         "\t(Assisted) Pull-Ups and Dips     3 x AMRAP "
#             thursday = "LEGS/GLUTES\n" \
#                        "\tSquats                            16 x 14 x 12\n" \
#                        "\tHip Thrusts                       20 x 15 x 10\n" \
#                        "\tRomanian Deadlifts                 16 x 14 x 12\n" \
#                        "\tQuad Extensions                   18 x 16 x 14\n" \
#                        "\tCalf Raises                       20 x 20 x 20 "
#             friday = "REST"
#             saturday = "REST"
#         elif self.gender == 'F' and self.goal == 'M':
#             sunday = "REST"
#             monday = "LEGS/GLUTES\n" \
#                      "\tSquats                              16 x 14 x 12\n" \
#                      "\tHip Thrusts                         20 x 15 x 10\n" \
#                      "\tRomanian Deadlifts                   16 x 14 x 12\n" \
#                      "\tQuad Extensions                     18 x 16 x 14\n" \
#                      "\tCalf Raises                         20 x 20 x 20 "
#             tuesday = "UPPER BODY\n" \
#                       "\t(Assisted) Pull-Ups                3 x AMRAP\n" \
#                       "\tDumbbell Press                     18 x 16 x 14\n" \
#                       "\tDumbbell Shoulder Press            18 x 16 x 14\n" \
#                       "\tPec Dec                            18 x 16 x 14\n" \
#                       "\tReverse Pec Dec                    18 x 16 x 14 "
#             wednesday = "ARMS/ABS\n" \
#                         "\tBarbell Curls                    18 x 16 x 14\n" \
#                         "\tSkullcrushers                    18 x 16 x 14\n" \
#                         "\tCable Curls                      18 x 16 x 14\n" \
#                         "\tTricep Pulldown                  18 x 16 x 14\n" \
#                         "\t(Assisted) Pull-Ups and Dips     3 x AMRAP "
#             thursday = "LEGS/GLUTES\n" \
#                        "\tSquats                            16 x 14 x 12\n" \
#                        "\tHip Thrusts                       20 x 15 x 10\n" \
#                        "\tRomanian Deadlift                 16 x 14 x 12\n" \
#                        "\tQuad Extensions                   18 x 16 x 14\n" \
#                        "\tCalf Raises                       20 x 20 x 20 "
#             friday = "REST"
#             saturday = "REST"
#         else:
#             sunday = "REST"
#             monday = "LEGS/GLUTES\n" \
#                      "\tSquats                              12 x 10 x 8\n" \
#                      "\tHip Thrusts                         16 x 14 x 12\n" \
#                      "\tRomanian Deadlift                   12 x 10 x 8\n" \
#                      "\tQuad Extensions                     14 x 12 x 10\n" \
#                      "\tCalf Raises                         14 x 12 x 10 "
#             tuesday = "UPPER BODY\n" \
#                       "\t(Assisted) Pull-Ups                3 x AMRAP\n" \
#                       "\tDumbbell Press                     14 x 12 x 10\n" \
#                       "\tDumbbell Shoulder Press            14 x 12 x 10\n" \
#                       "\tPec Dec                            14 x 12 x 10\n" \
#                       "\tReverse Pec Dec                    14 x 12 x 10 "
#             wednesday = "ARMS/ABS\n" \
#                         "\tBarbell Curls                    16 x 14 x 12\n" \
#                         "\tSkullcrushers                    16 x 14 x 12\n" \
#                         "\tCable Curls                      16 x 14 x 12\n" \
#                         "\tTricep Pulldown                  16 x 14 x 12\n" \
#                         "\t(Assisted) Pull-Ups and Dips     3 x AMRAP "
#             thursday = "LEGS/GLUTES\n" \
#                        "\tSquats                            12 x 10 x 8\n" \
#                        "\tHip Thrusts                       16 x 14 x 12\n" \
#                        "\tRomanian Deadlifts                12 x 10 x 8\n" \
#                        "\tQuad Extensions                   14 x 12 x 10\n" \
#                        "\tCalf Raises                       14 x 12 x 10 "
#             friday = "REST"
#             saturday = "REST"

#         plan = "SUNDAY:\t" + sunday + "\n" + "MONDAY:\t" \
#                + monday + "\n" + "TUESDAY:\t" + tuesday + "\n" + "WEDNESDAY:\t" + wednesday + "\n" + \
#                "THURSDAY:\t" + thursday + "\n" + "FRIDAY:\t" + friday + "\n" + "SATURDAY:\t" + saturday + \
#                "\n"

#         print(plan)

