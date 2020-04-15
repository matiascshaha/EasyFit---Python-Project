from PyQt5 import QtWidgets
import person
import workout
import sys


class EasyFitWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowTitle('EasyFit')
        self.heading = QtWidgets.QLabel('Welcome to EasyFit!', self)
        # This is where we need user input for height, weight, gender, and goal (weightloss, maintenance, or strength gain)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = EasyFitWindow()
    app.exec_()


