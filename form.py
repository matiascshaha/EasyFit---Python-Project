from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QRadioButton)
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
        self.heightLabel = QLineEdit()
        self.weightLabel = QLineEdit()
        self.goal = QLineEdit()
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
        self.setWindowTitle("EazyFit Window")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form Layout")
        layout = QFormLayout()
        self.hbox.addWidget(self.r1)
        self.hbox.addWidget(self.r2)
        self.hbox.addStretch()
        layout.addRow(QLabel("Name:"), self.nameLabel)
        layout.addRow(QLabel("Height:"), self.heightLabel)
        layout.addRow(QLabel("Weight:"), self.weightLabel)
        layout.addRow(QLabel("Workout Goal:"), self.goal)
        layout.addRow(QLabel("Gender:"), self.hbox)
        self.formGroupBox.setLayout(layout)

    def accept(self):
        n = self.nameLabel.text()
        h = self.heightLabel.text()
        w = self.weightLabel.text()
        g = self.goal.text()
        if self.r1.isChecked():
            gen = "M"
        else:
            gen = "F"
        # h, g, w, and gen each hold the user input height, goal, weight and gender as a str
        print(w)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    eazyFit = EasyFitWindow()
    sys.exit(eazyFit.exec())


# from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
#                              QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
#                              QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
#                              QVBoxLayout, QRadioButton)
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
#         self.heightLabel = QLineEdit()
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
#         self.setWindowTitle("EazyFit Window")

#     def createFormGroupBox(self):
#         self.formGroupBox = QGroupBox("Form Layout")
#         layout = QFormLayout()
#         self.hbox.addWidget(self.r1)
#         self.hbox.addWidget(self.r2)
#         self.hbox.addStretch()
#         self.gbox.addWidget(self.goal1)
#         self.gbox.addWidget(self.goal2)
#         self.gbox.addWidget(self.goal3)
#         self.gbox.addStretch()

#         layout.addRow(QLabel("Name:"), self.nameLabel)
#         layout.addRow(QLabel("Height:"), self.heightLabel)
#         layout.addRow(QLabel("Weight:"), self.weightLabel)
#         layout.addRow(QLabel("Workout Goal:"), self.gbox)
#         layout.addRow(QLabel("Gender:"), self.hbox)
#         self.formGroupBox.setLayout(layout)

#     def accept(self):
#         n = self.nameLabel.text()
#         h = self.heightLabel.text()
#         w = self.weightLabel.text()
#         if self.goal1.isChecked():
#             g = "C"
#         elif self.goal2.isChecked():
#             g = "M"
#         else:
#             g = "B"
#         if self.r1.isChecked():
#             gen = "M"
#         else:
#             gen = "F"
#         # h, g, w, and gen each hold the user input height, goal, weight and gender as a str
#         print(w)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     eazyFit = EasyFitWindow()
#     sys.exit(eazyFit.exec())
