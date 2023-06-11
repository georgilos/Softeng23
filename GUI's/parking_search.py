import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QRadioButton, \
    QPushButton, QFrame, QHBoxLayout, QMessageBox, QGroupBox


class ParkingSearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Find Parking")
        self.setGeometry(100, 100, 400, 400)

        # Create the main title label
        title_label = QLabel("Find Parking", self)
        title_label.setStyleSheet("font-size: 20pt; font-weight: bold")
        title_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # Create the scroll area for parking options
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the radio buttons
        scroll_content = QWidget(scroll_area)
        scroll_area.setWidget(scroll_content)

        # Create a layout for the scroll content
        scroll_layout = QVBoxLayout(scroll_content)

        # Add radio buttons, names, addresses, and line separators for parking options
        parking_options = [
            {"name": "Auto Parking Patras", "address": "Gerokostopoulou Str. 12, Patras , 26500"},
            {"name": "Patras Parking", "address": "Ioannou Vlachou Str. 5, Patras, 26500"},
            {"name": "Car Parking", "address": "Karaiskaki Str. 41,Patras, 26500"},
            {"name": "Auto Parking Kefalas", "address": "Kanari Str. 74, Patras, 26500"},
            {"name": "Parking 1", "address": "Radinou Str. 1, Patra, 26221"},
            {"name": "Parking 2", "address": "Mourouzi Str. 13, Patra, 26223"},
            {"name": "Parking 3", "address": "Alimousiwn Str. 12, Athina, 11851"},
            {"name": "Parking 4", "address": "Sfakianakh Str. 9, Athina, 10445"}
        ]

        self.radio_buttons = []  # Keep track of radio buttons

        for option in parking_options:
            radio_button = QRadioButton(self)
            self.radio_buttons.append(radio_button)  # Add radio button to the list

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
        select_button.clicked.connect(self.select_parking)

        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.open_main_window)

        # Create a layout for the main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(select_button)
        main_layout.addWidget(back_button)

        # Set the main layout in the main window
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def select_parking(self):
        selected_button = None

        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                selected_button = radio_button
                break

        if selected_button is None:
            # Display an error message
            QMessageBox.warning(self, "Error", "Please select a parking.")
        else:
            # Perform the desired action when a parking is selected
            print("Parking selected:", selected_button.text())

            # Open the Spot Selection window
            self.spot_selection_window = SpotSelectionWindow()
            self.spot_selection_window.show()
            self.close()

    def open_main_window(self):
        from main_page import Ui_MainWindow
        self.main_page = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_page)
        self.main_page.show()
        self.close()


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

        # Connect the "Back" button click event to the handler
        self.back_button.clicked.connect(self.open_parking_search_window)

    def open_parking_search_window(self):
        self.parking_search_window = ParkingSearchWindow()
        self.parking_search_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParkingSearchWindow()
    window.show()
    sys.exit(app.exec_())
