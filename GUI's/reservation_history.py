import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QRadioButton, \
QPushButton, QFrame, QHBoxLayout
from PyQt5.QtGui import QColor

class ReservationHistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReservationHistoryWindow")
        self.setGeometry(100, 100, 400, 400)

        # Create the main title label
        title_label = QLabel("Your Past Reservations!", self)
        title_label.setStyleSheet("font-size: 20pt; font-weight: bold")
        title_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # Create the scroll area for parking options
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the radio buttons
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        # Create a layout for the scroll content
        scroll_layout = QVBoxLayout(scroll_content)

        # Add radio buttons, names, addresses, and line separators for parking options
        parking_options = [
            {"name": "Parking 1", "address": "Radinou  1, Patra, 26221                                     23/06/2023"},
            {"name": "Parking 2", "address": "Mourouzi 13, Patra, 26223                                  19/06/2023"},
            {"name": "Parking 3", "address": "Alimousiwn 12, Athina, 11851                             12/05/2023"},
            {"name": "Parking 4", "address": "Sfakianakh 9, Athina, 10445                                06/05/2023"},
        ]

        for option in parking_options:
            radio_button = QRadioButton(self)
            name_label = QLabel(option["name"], self)
            name_label.setStyleSheet("font-size: 12pt; font-weight: bold")
            name_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

            address_label = QLabel(option["address"], self)
            address_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

            # Create a layout for the radio button and name
            option_layout = QHBoxLayout()
            option_layout.addWidget(radio_button)
            option_layout.addWidget(name_label)
            option_layout.addStretch()

            scroll_layout.addLayout(option_layout)
            scroll_layout.addWidget(address_label)

            # Add a line separator after each parking option
            line_separator = QFrame(self)
            line_separator.setFrameShape(QFrame.HLine)
            line_separator.setFrameShadow(QFrame.Sunken)
            scroll_layout.addWidget(line_separator)

        # Create the Select Parking and Back buttons
        select_button = QPushButton("Select Parking", self)
        select_button.clicked.connect(self.chooseSpot)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.open_main_window)

        delete_history_button = QPushButton("Delete History", self)
        delete_history_button.clicked.connect(self.deleteHistory)
        delete_history_button.setStyleSheet("color: red")

        # Create a layout for the main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(select_button)
        main_layout.addWidget(back_button)
        main_layout.addWidget(delete_history_button)

        # Set the main layout in the main window
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Disable the labels containing "Disabled Typical user" and "Electrical vehicle"
        for label in central_widget.findChildren(QLabel):
            if "Disabled Typical user" in label.text() or "Electrical vehicle" in label.text():
                label.setEnabled(False)

    def chooseSpot(self):
        print("Choose Spot method called")

    def deleteHistory(self):
        print("Delete History method called")

    def open_main_window(self):
        
        print("Open Main Window method called")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationHistoryWindow()
    window.show()
    sys.exit(app.exec_())






