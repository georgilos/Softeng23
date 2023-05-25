from PyQt5 import QtWidgets

class ParkingWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Parking")
        self.setGeometry(100, 100, 400, 300)

        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Select Parking")
        layout.addWidget(label)
        self.setLayout(layout)
