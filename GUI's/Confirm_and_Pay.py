from PyQt5 import QtCore, QtGui, QtWidgets

class ConfirmPayWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Confirm and Pay")
        self.setGeometry(100, 100, 400, 300)

        self.personal_info = {
            "card_number": "",
            "expired_date": "",
            "cvv": ""
        }

        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()

        # Create labels and line edits for personal information
        self.label_card_number = QtWidgets.QLabel("Card Number:")
        self.line_card_number= QtWidgets.QLineEdit()

        self.label_expired_date = QtWidgets.QLabel("Expired Date:")
        self.line_expired_date = QtWidgets.QLineEdit()

        self.label_cvv = QtWidgets.QLabel("CVV:")
        self.line_cvv = QtWidgets.QLineEdit()

        # Create a button to update personal information
        btn_change_info = QtWidgets.QPushButton("Change Personal Info")
        btn_change_info.clicked.connect(self.changePersonalInfo)

        # Create a button to cancel the reservation
        btn_cancel_reservation = QtWidgets.QPushButton("Cancel Reservation")
        btn_cancel_reservation.clicked.connect(self.cancelReservation)

        # Create a button to confirm payment
        btn_confirm_payment = QtWidgets.QPushButton("Confirm Payment")
        btn_confirm_payment.clicked.connect(self.confirmPayment)
        btn_confirm_payment.clicked.connect(self.inTime)
        btn_confirm_payment.clicked.connect(self.outOfTime)

        # Add the widgets to the main layout
        main_layout.addWidget(self.label_card_number)
        main_layout.addWidget(self.line_card_number)
        main_layout.addWidget(self.label_expired_date)
        main_layout.addWidget(self.line_expired_date)
        main_layout.addWidget(self.label_cvv)
        main_layout.addWidget(self.line_cvv)
        main_layout.addWidget(btn_change_info)
        main_layout.addWidget(btn_confirm_payment)
        main_layout.addWidget(btn_cancel_reservation)

        # Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def showPersonalInfo(self):
        # Function to display the personal information
        self.line_name.setText(self.personal_info["card_number"])
        self.line_email.setText(self.personal_info["expired_date"])
        self.line_address.setText(self.personal_info["cvv"])

    def changePersonalInfo(self):
        # Function to open a dialog for changing personal information
        dialog = PersonalInfoDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.personal_info["card_number"] = dialog.card_number
            self.personal_info["expired_date"] = dialog.expired_date
            self.personal_info["cvv"] = dialog.cvv
            self.changePersonalInfo()

    # def unchangedPersonalInfo(self):


    def inTime(self):
        # Function to display a message box indicating being on time
        QtWidgets.QMessageBox.information(self, "On Time", "You are in time for your reservation.")

    def outOfTime(self):
        # Function to display a message box indicating being on time
        QtWidgets.QMessageBox.information(self, "Out of Time", "You are out of time for your reservation. You have extra charge")

    


    def confirmPayment(self):
        # Function to handle payment confirmation
        QtWidgets.QMessageBox.information(self, "Payment Confirmed", "Payment has been confirmed.")

    def showPaymentProblem(self):
        # Function to handle payment problem
        QtWidgets.QMessageBox.information(self, "Payment Problem")

    def cancelReservation(self):
        # Function to cancel the reservation
        QtWidgets.QMessageBox.information(self, "Your reservation has been canceled!")

    def returnNumberPoints(self):
        QtWidgets.QMessageBox.information(self, "Your Points will be added on the system")
         

class PersonalInfoDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Personal Info")

        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()

        # Create line edits for personal information
        self.line_name = QtWidgets.QLineEdit()
        self.line_email = QtWidgets.QLineEdit()
        self.line_address = QtWidgets.QLineEdit()

        # Add the line edits to the main layout
        main_layout.addWidget(QtWidgets.QLabel("Name:"))
        main_layout.addWidget(self.line_name)
        main_layout.addWidget(QtWidgets.QLabel("Email:"))
        main_layout.addWidget(self.line_email)
        main_layout.addWidget(QtWidgets.QLabel("Address:"))
        main_layout.addWidget(self.line_address)

        # Create buttons for accepting or rejecting changes
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout.addWidget(button_box)

        # Set the main layout for the dialog
        self.setLayout(main_layout)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    parkare_to = ConfirmPayWindow()
    parkare_to.show()
    sys.exit(app.exec_())

       
