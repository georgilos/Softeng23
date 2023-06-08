import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton


class ReservationHistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reservation History")

        # Create a table widget
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Parking Lot", "Date", "Status"])

        # Add some example data
        self.add_reservation("Lot A", "2023-06-01", "Completed")
        self.add_reservation("Lot B", "2023-06-03", "Canceled")

        # Create a button for adding reservations
        self.add_reservation_button = QPushButton("Add Reservation")
        self.add_reservation_button.clicked.connect(self.add_reservation_dialog)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_reservation_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

    def add_reservation(self, parking_lot, date, status):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

        self.table.setItem(row_count, 0, QTableWidgetItem(parking_lot))
        self.table.setItem(row_count, 1, QTableWidgetItem(date))
        self.table.setItem(row_count, 2, QTableWidgetItem(status))

    def add_reservation_dialog(self):
        # Implement your logic for adding reservations
        # This is just a placeholder function
        print("Add reservation dialog")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    reservation_history = ReservationHistoryWindow()
    reservation_history.show()
    sys.exit(app.exec_())