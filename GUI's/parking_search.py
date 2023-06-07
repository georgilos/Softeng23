import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QRadioButton, \
    QPushButton, QFrame


class MainWindow(QMainWindow):
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

        # Create a layout for the radio buttons
        scroll_layout = QVBoxLayout(scroll_content)

        # Add radio buttons and line separators for parking options
        parking_options = ["Parking 1", "Parking 2", "Parking 3", "Parking 4", "Parking 5", "Parking 6",
                           "Parking 7", "Parking 8", "Parking 9"]
        for option in parking_options:
            radio_button = QRadioButton(option, self)
            scroll_layout.addWidget(radio_button)

            # Add a line separator after each radio button
            line_separator = QFrame(self)
            line_separator.setFrameShape(QFrame.HLine)
            line_separator.setFrameShadow(QFrame.Sunken)
            scroll_layout.addWidget(line_separator)

        # Create the Select Parking and Back buttons
        select_button = QPushButton("Select Parking", self)
        back_button = QPushButton("Back", self)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
