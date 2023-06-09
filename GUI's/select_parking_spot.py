import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QRadioButton, QPushButton, QGroupBox
from parking_search import ParkingSearchWindow


class SpotSelectionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spot Selection")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_label = QLabel("Select your spot type", self)
        self.title_label.setStyleSheet("font-weight: bold; font-size: 16px")
        self.title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.layout.addWidget(self.title_label)

        self.spot_group = QGroupBox(self)
        self.spot_group_layout = QHBoxLayout()
        self.basic_radio = QRadioButton("Basic spot", self)
        self.electric_radio = QRadioButton("Electric car spot", self)
        self.handicap_radio = QRadioButton("Handicap spot", self)
        self.spot_group_layout.addWidget(self.basic_radio)
        self.spot_group_layout.addWidget(self.electric_radio)
        self.spot_group_layout.addWidget(self.handicap_radio)
        self.spot_group.setLayout(self.spot_group_layout)
        self.layout.addWidget(self.spot_group)

        self.button_layout = QHBoxLayout()
        self.back_button = QPushButton("Back", self)
        self.continue_button = QPushButton("Continue", self)
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.continue_button)
        self.layout.addLayout(self.button_layout)

        self.layout.addStretch()

        # Connect to the "Back" button click event to the handler
        self.back_button.clicked.connect(self.open_parking_search_window)

    def open_parking_search_window(self):
        self.parking_search_window = ParkingSearchWindow()
        self.parking_search_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpotSelectionWindow()
    window.show()
    sys.exit(app.exec_())
