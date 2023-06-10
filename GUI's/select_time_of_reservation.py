from PyQt5 import QtCore, QtGui, QtWidgets


class ReservationTime(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reservation Time")
        self.duration = None

        self.label_select_time = QtWidgets.QLabel("Select Reservation Time:")

        self.radio_group = QtWidgets.QButtonGroup()


        self.label_select_time = QtWidgets.QLabel("Select Reservation Time:")
        self.combo_box_time = QtWidgets.QComboBox()
        self.combo_box_time.addItem("1 hour")
        self.combo_box_time.addItem("2 hours")
        self.combo_box_time.addItem("3 hours")

        self.radio_10am = QtWidgets.QRadioButton("10:00 AM")
        self.radio_11am = QtWidgets.QRadioButton("11:00 AM")
        self.radio_12pm = QtWidgets.QRadioButton("12:00 PM")
        self.radio_1pm = QtWidgets.QRadioButton("1:00 PM")

        self.radio_group.addButton(self.radio_10am)
        self.radio_group.addButton(self.radio_11am)
        self.radio_group.addButton(self.radio_12pm)
        self.radio_group.addButton(self.radio_1pm)

        self.button_choose_time = QtWidgets.QPushButton("Choose Time")
        self.button_choose_time.clicked.connect(self.chooseDurationTime)

        self.button_show_available_time = QtWidgets.QPushButton("Show Available Time")
        self.button_show_available_time.clicked.connect(self.showAvailableReservationTime)

        self.button_confirm = QtWidgets.QPushButton("Confirm")
        self.button_confirm.clicked.connect(self.confirmTimeDetails)

        self.button_update = QtWidgets.QPushButton("Update")
        self.button_update.clicked.connect(self.systemUpdate)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label_select_time)
        layout.addWidget(self.combo_box_time)
        layout.addWidget(self.label_select_time)
        layout.addWidget(self.radio_10am)
        layout.addWidget(self.radio_11am)
        layout.addWidget(self.radio_12pm)
        layout.addWidget(self.radio_1pm)
        layout.addWidget(self.button_choose_time)
        layout.addWidget(self.button_show_available_time)
        layout.addWidget(self.button_confirm)
        layout.addWidget(self.button_update)
        self.setLayout(layout)

    def chooseDurationTime(self):
        # Function to handle the selection of reservation time
        selected_button = self.radio_group.checkedButton()
        if selected_button:
            self.duration = selected_button.text()
            QtWidgets.QMessageBox.information(self, "Reservation Time", f"Selected reservation time: {self.duration}")
        else:
            QtWidgets.QMessageBox.warning(self, "No Time Selected", "Please select a reservation time.")

    def showAvailableReservationTime(self):
        # Function to show the available reservation times
        # Implement your logic here to retrieve and display the available times
        available_times = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM"]
        time_info = "Available Reservation Times:\n"
        for time in available_times:
            time_info += f"- {time}\n"
        QtWidgets.QMessageBox.information(self, "Available Reservation Times", time_info)

    def correctDuration(self):
        # Function to handle the case when the selected duration is valid
        QtWidgets.QMessageBox.information(self, "Valid Duration", "The selected duration is valid.")
    
    def wrongDurationTime(self):
        # Function to handle the case when the selected duration is invalid
        QtWidgets.QMessageBox.warning(self, "Invalid Duration", "The selected duration is invalid. Please choose a different duration.")

    def systemUpdate(self):
        # Function to update 
         QtWidgets.QMessageBox.warning(self, "Updated System")

    
    def editDurationTime(self):
        # Function to edit
    
        QtWidgets.QMessageBox.warning(self, "Your Duration Time is modified!")

    def showTimeDetails(self):
        # Function to show time details
    
        QtWidgets.QMessageBox.warning(self, "Show Time details")

    
    def confirmTimeDetails(self):
        # Function to confirm time details
    
       QtWidgets.QMessageBox.warning(self, "Your Time Details are confirmed")


    

        




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    reservation_time = ReservationTime()
    reservation_time.show()
    sys.exit(app.exec_())