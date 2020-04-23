from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                              QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                              QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                              QVBoxLayout, QRadioButton, QWidget,QButtonGroup)
import person
import workout
import sys

class EasyFitWindow(QDialog):
    numGridRows = 3
    numButtons = 4

    def __init__(self):
        super(EasyFitWindow, self).__init__()
        self.hbox = QHBoxLayout()
        self.nameLabel = QLineEdit()
        self.ageLabel = QLineEdit()
        self.feetLabel = QLineEdit()
        self.inchesLabel = QLineEdit()
        self.weightLabel = QLineEdit()
        self.gbox = QHBoxLayout()
        # self.goal = QLineEdit()
        self.goal1 = QRadioButton("Weight Loss")
        self.goal2 = QRadioButton("Maintenance")
        self.goal3 = QRadioButton("Strength Gain")
        self.r1 = QRadioButton("Male")
        self.r2 = QRadioButton("Female")
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("EasyFit")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        self.genGroup = QButtonGroup(self.formGroupBox)
        self.goalGroup = QButtonGroup(self.formGroupBox)
        self.genGroup.addButton(self.r1)
        self.genGroup.addButton(self.r2)
        self.goalGroup.addButton(self.goal1)
        self.goalGroup.addButton(self.goal2)
        self.goalGroup.addButton(self.goal3)
        layout = QFormLayout()
        self.hbox.addWidget(self.r1)
        self.hbox.addWidget(self.r2)
        self.hbox.addStretch()
        self.gbox.addWidget(self.goal1)
        self.gbox.addWidget(self.goal2)
        self.gbox.addWidget(self.goal3)
        self.gbox.addStretch()

        layout.addRow(QLabel("Name:"), self.nameLabel)
        layout.addRow(QLabel("Age:"), self.ageLabel)
        layout.addRow(QLabel("Height:   (feet)"), self.feetLabel)
        layout.addRow(QLabel("          (inches)"), self.inchesLabel)
        layout.addRow(QLabel("Weight:"), self.weightLabel)
        layout.addRow(QLabel("Workout Goal:"), self.gbox)
        layout.addRow(QLabel("Gender:"), self.hbox)
        self.formGroupBox.setLayout(layout)

    def accept(self):
        n = self.nameLabel.text()
        a = int(self.ageLabel.text())
        h = 12 * int(self.feetLabel.text()) + int(self.inchesLabel.text())
        w = int(self.weightLabel.text())
        if self.goal1.isChecked():
            g = 'C'
        elif self.goal2.isChecked():
            g = 'M'
        else:
            g = 'B'
        if self.r1.isChecked():
            gen = 'M'
        else:
            gen = 'F'
         # h, g, w, and gen each hold the user input height, goal, weight and gender as a str
        # print(n)
        # print(h)
        # print(w)
        # print(g)
        # print(gen)
        p = person.Person(n, a, h, w, g, gen)
        p.diet.print_Diet()
        p.workout.printWorkout()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    eazyFit = EasyFitWindow()
    sys.exit(eazyFit.exec())


# from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
#                               QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
#                               QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
#                               QVBoxLayout, QRadioButton, QWidget,QButtonGroup)
# import person
# import workout
# import sys

# class EasyFitWindow(QDialog):
#     numGridRows = 3
#     numButtons = 4

#     def __init__(self):
#         super(EasyFitWindow, self).__init__()
#         self.hbox = QHBoxLayout()
#         self.nameLabel = QLineEdit()
#         self.feetLabel = QLineEdit()
#         self.inchesLabel = QLineEdit()
#         self.weightLabel = QLineEdit()
#         self.gbox = QHBoxLayout()
#         # self.goal = QLineEdit()
#         self.goal1 = QRadioButton("Weight Loss")
#         self.goal2 = QRadioButton("Maintenance")
#         self.goal3 = QRadioButton("Strength Gain")
#         self.r1 = QRadioButton("Male")
#         self.r2 = QRadioButton("Female")
#         self.createFormGroupBox()
#         buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
#         buttonBox.accepted.connect(self.accept)
#         buttonBox.rejected.connect(self.reject)
#         mainLayout = QVBoxLayout()
#         mainLayout.addWidget(self.formGroupBox)
#         mainLayout.addWidget(buttonBox)
#         self.setLayout(mainLayout)
#         self.setWindowTitle("EasyFit")

#     def createFormGroupBox(self):
#         self.formGroupBox = QGroupBox()
#         self.genGroup = QButtonGroup(self.formGroupBox)
#         self.goalGroup = QButtonGroup(self.formGroupBox)
#         self.genGroup.addButton(self.r1)
#         self.genGroup.addButton(self.r2)
#         self.goalGroup.addButton(self.goal1)
#         self.goalGroup.addButton(self.goal2)
#         self.goalGroup.addButton(self.goal3)
#         layout = QFormLayout()
#         self.hbox.addWidget(self.r1)
#         self.hbox.addWidget(self.r2)
#         self.hbox.addStretch()
#         self.gbox.addWidget(self.goal1)
#         self.gbox.addWidget(self.goal2)
#         self.gbox.addWidget(self.goal3)
#         self.gbox.addStretch()

#         layout.addRow(QLabel("Name:"), self.nameLabel)
#         layout.addRow(QLabel("Height:   (feet)"), self.feetLabel)
#         layout.addRow(QLabel("          (inches)"), self.inchesLabel)
#         layout.addRow(QLabel("Weight:"), self.weightLabel)
#         layout.addRow(QLabel("Workout Goal:"), self.gbox)
#         layout.addRow(QLabel("Gender:"), self.hbox)
#         self.formGroupBox.setLayout(layout)

#     def accept(self):
#         n = self.nameLabel.text()
#         h = 12 * int(self.feetLabel.text()) + int(self.inchesLabel.text())
#         w = int(self.weightLabel.text())
#         if self.goal1.isChecked():
#             g = 'C'
#         elif self.goal2.isChecked():
#             g = 'M'
#         else:
#             g = 'B'
#         if self.r1.isChecked():
#             gen = 'M'
#         else:
#             gen = 'F'
#          # h, g, w, and gen each hold the user input height, goal, weight and gender as a str
#         print(n)
#         print(h)
#         print(w)
#         print(g)
#         print(gen)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     eazyFit = EasyFitWindow()
#     sys.exit(eazyFit.exec())



