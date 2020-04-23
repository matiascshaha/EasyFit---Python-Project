import sys
import subprocess, os, platform

from PyQt5.QtWidgets import (QApplication, QDialog,
                             QDialogButtonBox, QFormLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QVBoxLayout, QRadioButton, QButtonGroup)

import person


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
        self.goal1 = QRadioButton("Weight Loss")
        self.goal2 = QRadioButton("Maintenance")
        self.goal3 = QRadioButton("Strength Gain")
        self.r1 = QRadioButton("Male")
        self.r2 = QRadioButton("Female")
        self.fileLabel = QLineEdit()
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
        layout.addRow(QLabel("Output File Name:"), self.fileLabel)
        layout.addWidget(QLabel("(without file extension)"))
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
        filename = self.fileLabel.text() + ".txt"

        p = person.Person(n, a, h, w, g, gen)

        f = open(filename, 'w')

        plan = "\t\tDAILY DIET PLAN FOR " + n.upper() + ":\n\n" + p.diet.print_Diet() + \
               "\n\n\n\n\n\t\tWORKOUT PLAN FOR " + n.upper() + ":\n\n" + p.workout.printWorkout()

        f.write(plan)
        f.close()

        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', filename))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(filename)
        else:  # linux variants
            subprocess.call(('xdg-open', filename))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    eazyFit = EasyFitWindow()
    sys.exit(eazyFit.exec())


# import sys

# from PyQt5.QtWidgets import (QApplication, QDialog,
#                              QDialogButtonBox, QFormLayout, QGroupBox, QHBoxLayout,
#                              QLabel, QLineEdit, QVBoxLayout, QRadioButton, QButtonGroup)

# import person


# class EasyFitWindow(QDialog):
#     numGridRows = 3
#     numButtons = 4

#     def __init__(self):
#         super(EasyFitWindow, self).__init__()
#         self.hbox = QHBoxLayout()
#         self.nameLabel = QLineEdit()
#         self.ageLabel = QLineEdit()
#         self.feetLabel = QLineEdit()
#         self.inchesLabel = QLineEdit()
#         self.weightLabel = QLineEdit()
#         self.gbox = QHBoxLayout()
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
#         layout.addRow(QLabel("Age:"), self.ageLabel)
#         layout.addRow(QLabel("Height:   (feet)"), self.feetLabel)
#         layout.addRow(QLabel("          (inches)"), self.inchesLabel)
#         layout.addRow(QLabel("Weight:"), self.weightLabel)
#         layout.addRow(QLabel("Workout Goal:"), self.gbox)
#         layout.addRow(QLabel("Gender:"), self.hbox)
#         self.formGroupBox.setLayout(layout)

#     def accept(self):
#         n = self.nameLabel.text()
#         a = int(self.ageLabel.text())
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

#         p = person.Person(n, a, h, w, g, gen)
#         print("\t\t", "DAILY DIET PLAN FOR ", n.upper(), ":")
#         p.diet.print_Diet()
#         print("\n\n\t\t", "WORKOUT PLAN FOR ", n.upper(), ":")
#         p.workout.printWorkout()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     eazyFit = EasyFitWindow()
#     sys.exit(eazyFit.exec())



