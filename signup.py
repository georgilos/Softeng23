from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 637)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 50, 271, 528))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(self.layoutWidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.firstname_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.firstname_line.setObjectName("firstname_line")
        self.gridLayout.addWidget(self.firstname_line, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.lastname_label = QtWidgets.QLabel(self.layoutWidget)
        self.lastname_label.setObjectName("lastname_label")
        self.gridLayout.addWidget(self.lastname_label, 2, 0, 1, 1)
        self.lastname_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.lastname_line.setObjectName("lastname_line")
        self.gridLayout.addWidget(self.lastname_line, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(18, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 3, 2, 1, 1)
        self.username_label = QtWidgets.QLabel(self.layoutWidget)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 4, 0, 1, 1)
        self.username_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.username_line.setObjectName("username_line")
        self.gridLayout.addWidget(self.username_line, 4, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 5, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 2, 1, 1)
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 6, 0, 1, 1)
        self.pass_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.pass_line.setObjectName("pass_line")
        self.gridLayout.addWidget(self.pass_line, 6, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 7, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 7, 2, 1, 1)
        self.email_label = QtWidgets.QLabel(self.layoutWidget)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 8, 0, 1, 1)
        self.email_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.email_line.setObjectName("email_line")
        self.gridLayout.addWidget(self.email_line, 8, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 9, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 9, 2, 1, 1)
        self.phone_num_label = QtWidgets.QLabel(self.layoutWidget)
        self.phone_num_label.setObjectName("phone_num_label")
        self.gridLayout.addWidget(self.phone_num_label, 10, 0, 1, 1)
        self.phone_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.phone_line.setObjectName("phone_line")
        self.gridLayout.addWidget(self.phone_line, 10, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 11, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 11, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 3, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 4, 0, 1, 1)
        self.register_button = QtWidgets.QPushButton(self.layoutWidget)
        self.register_button.setObjectName("register_button")
        self.gridLayout_2.addWidget(self.register_button, 4, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 4, 2, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(23)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Registration "))
        self.name_label.setText(_translate("MainWindow", "First name "))
        self.lastname_label.setText(_translate("MainWindow", "Lastname"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.email_label.setText(_translate("MainWindow", "Email "))
        self.phone_num_label.setText(_translate("MainWindow", "Phone number"))
        self.register_button.setText(_translate("MainWindow", "Register"))


        self.register_button.clicked.connect(self.register_user)

    def register_user(self):
        # Get user input from the UI elements
        name = self.firstname_line.text()
        lastname = self.lastname_line.text()
        username = self.username_line.text()
        password = self.pass_line.text()
        email = self.email_line.text()
        phone_number = self.phone_line.text()

        # Create a database connection
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="Test@123",
            database="softeng"
        )

        # Perform the database operation
        cursor = db.cursor()
        query = "INSERT INTO users (name, lastname, username, password, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, lastname, username, password, email, phone_number)
        cursor.execute(query, values)

        # Commit the changes and close the database connection
        db.commit()
        db.close()

        # Display a success message or perform any other actions
        QtWidgets.QMessageBox.information(MainWindow, "Registration Successful", "User registered successfully!")

        # Clear the input fields
        self.firstname_line.clear()
        self.lastname_line.clear()
        self.username_line.clear()
        self.pass_line.clear()
        self.email_line.clear()
        self.phone_line.clear()

        # Optionally, you can close the window or perform any other actions after registration

        # to run as python script
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())