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
        hbox = QHBoxLayout()
        r1 = QRadioButton("Male")
        r2 = QRadioButton("Female")
        hbox.addWidget(r1)
        hbox.addWidget(r2)
        hbox.addStretch()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Height:"), QLineEdit())
        layout.addRow(QLabel("Workout Goal:"), QLineEdit())
        layout.addRow(QLabel("Gender:"), hbox)
        self.formGroupBox.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    eazyFit = EasyFitWindow()
    sys.exit(eazyFit.exec())
