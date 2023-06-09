from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.name = "Giannis"
        self.username = "John" 
        self.lastname = "Papadopoulos"
        self.email = "johnpap@gmail.com"
        self.vehicleid = "AZK-8309"
        
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("Change User Details Window")
        self.resize(400, 200)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
      # Name 
        self.label_name = QtWidgets.QLabel("Name:", self)
        self.layout.addWidget(self.label_name)

        self.line_name = QtWidgets.QLineEdit(self)
        self.line_name.setText(self.name)
        self.layout.addWidget(self.line_name)


    # Lastname 

        self.label_lastname = QtWidgets.QLabel("Lastname:", self)
        self.layout.addWidget(self.label_lastname)

        self.line_lastname = QtWidgets.QLineEdit(self)
        self.line_lastname.setText(self.lastname)
        self.layout.addWidget(self.line_lastname)

        self.button_change_lastname = QtWidgets.QPushButton("Change Lastname", self)
        self.button_change_lastname.clicked.connect(self.change_lastname)
        self.layout.addWidget(self.button_change_lastname)


    # Email 

        self.label_email = QtWidgets.QLabel("Email:", self)
        self.layout.addWidget(self.label_email)

        self.line_email = QtWidgets.QLineEdit(self)
        self.line_email.setText(self.email)
        self.layout.addWidget(self.line_email)

        self.button_change_email = QtWidgets.QPushButton("Change Email", self)
        self.button_change_email.clicked.connect(self.change_email)
        self.layout.addWidget(self.button_change_email)
      


    # Username
        self.label_username = QtWidgets.QLabel("Username:", self)
        self.layout.addWidget(self.label_username)
        
        self.line_username = QtWidgets.QLineEdit(self)
        self.line_username.setText(self.username)
        self.layout.addWidget(self.line_username)
    # Password
        self.label_password = QtWidgets.QLabel("Password:", self)
        self.layout.addWidget(self.label_password)
        
        self.line_password = QtWidgets.QLineEdit(self)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.line_password)

    # VehicleID
        self.label_vehicleid = QtWidgets.QLabel("VehicleID:", self)
        self.layout.addWidget(self.label_vehicleid)
        self.line_vehicleid = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.line_vehicleid)
      
   
    # Buttons
        self.button_change_name = QtWidgets.QPushButton("Change Name", self)
        self.button_change_name.clicked.connect(self.change_name)
        self.layout.addWidget(self.button_change_name)

        self.button_change_username = QtWidgets.QPushButton("Change Username", self)
        self.button_change_username.clicked.connect(self.change_username)
        self.layout.addWidget(self.button_change_username)
        
        self.button_change_password = QtWidgets.QPushButton("Change Password", self)
        self.button_change_password.clicked.connect(self.change_password)
        self.layout.addWidget(self.button_change_password)
        
        
        self.button_change_vehicleid = QtWidgets.QPushButton("Change VehicleID", self)
        self.button_change_vehicleid.clicked.connect(self.change_vehicleid)
        self.layout.addWidget(self.button_change_vehicleid)


        self.updateButton = QtWidgets.QPushButton("Update", self)
        self.updateButton.clicked.connect(self.updateNewInfo)
        self.layout.addWidget(self.updateButton)
        
        self.show()
    
    #Change Name function
    def change_name(self):
        new_name = self.line_name.text()
        self.name = new_name
        QtWidgets.QMessageBox.information(self, "Name Changed", "Name has been changed to: {}".format(new_name))

    #change lastname function
    def change_lastname(self):
        new_lastname = self.line_lastname.text()
        self.lastname = new_lastname
        QtWidgets.QMessageBox.information(self, "LastName Changed", "LastName has been changed to: {}".format(new_lastname))

    #change email function
    def change_email(self):
        new_email = self.line_email.text()
        self.email = new_email
        QtWidgets.QMessageBox.information(self, "Email Changed", "Email has been changed to: {}".format(new_email))

    #Change username function
    def change_username(self):
        new_username = self.line_username.text()
        self.username = new_username
        QtWidgets.QMessageBox.information(self, "Username Changed", "Username has been changed to: {}".format(new_username))
    
    #Change password function
    def change_password(self):
        new_password = self.line_password.text()
        self.password = new_password
        QtWidgets.QMessageBox.information(self, "Password Changed", "Password has been changed to: {}".format(new_password))

    #change vehicleid function
    def change_vehicleid(self):
        new_vehicleid= self.line_username.text()
        self.vehicleid = new_vehicleid
        QtWidgets.QMessageBox.information(self, "VehicleID Changed", "VehicleID has been changed to: {}".format(new_vehicleid))
    
    #show current info function
    def showCurrentInfo(self):
        QtWidgets.QMessageBox.warning(self, "Show User Details", "User details: Username - {}, Password - {}".format(self.username, self.password))

    #show Personal user info funtion
    def editPersonalInfo(self):
        QtWidgets.QMessageBox.warning(self, "Show Edit Details", "User details: Username - {}, Password - {}".format(self.username, self.password))
    
    #Update New Info function
    def updateNewInfo(self):
        QtWidgets.QMessageBox.information(self, "Update", "Your details are updated")

    #Wrong password function
    def wrong_password(self):
        QtWidgets.QMessageBox.warning(self, "Wrong Password", "Invalid password. Please try again.")
    
    #wrong card info function
    def wrong_CardInfo(self):
        QtWidgets.QMessageBox.warning(self, "Wrong CardInfo", "Invalid card info. Please try again.")
    
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
