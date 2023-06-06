from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.name = "Giannis"
        self.username = "John"  # Initial username
        
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("Change User Details Window")
        self.resize(400, 200)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
      #Name 
        self.label_name = QtWidgets.QLabel("Name:", self)
        self.layout.addWidget(self.label_name)

        self.line_name = QtWidgets.QLineEdit(self)
        self.line_name.setText(self.name)
        self.layout.addWidget(self.line_name)
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
    
        self.button_change_name = QtWidgets.QPushButton("Change Name", self)
        self.button_change_name.clicked.connect(self.change_name)
        self.layout.addWidget(self.button_change_name)

        self.button_change_username = QtWidgets.QPushButton("Change Username", self)
        self.button_change_username.clicked.connect(self.change_username)
        self.layout.addWidget(self.button_change_username)
        
        self.button_change_password = QtWidgets.QPushButton("Change Password", self)
        self.button_change_password.clicked.connect(self.change_password)
        self.layout.addWidget(self.button_change_password)
        
        self.updateButton = QtWidgets.QPushButton("Update", self)
        self.updateButton.clicked.connect(self.updateNewInfo)
        self.layout.addWidget(self.updateButton)
        
        self.show()
    
    
    def change_name(self):
        new_name = self.line_name.text()
        self.username = new_name
        QtWidgets.QMessageBox.information(self, "Name Changed", "Name has been changed to: {}".format(new_name))

    def change_username(self):
        new_username = self.line_username.text()
        self.username = new_username
        QtWidgets.QMessageBox.information(self, "Username Changed", "Username has been changed to: {}".format(new_username))
    
    def change_password(self):
        new_password = self.line_password.text()
        self.password = new_password
        QtWidgets.QMessageBox.information(self, "Password Changed", "Password has been changed to: {}".format(new_password))
    
    def showCurrentInfo(self):
        QtWidgets.QMessageBox.warning(self, "Show User Details", "User details: Username - {}, Password - {}".format(self.username, self.password))
    
    def updateNewInfo(self):
        QtWidgets.QMessageBox.information(self, "Update", "Your details are updated")

    def wrong_password(self):
        QtWidgets.QMessageBox.warning(self, "Wrong Password", "Invalid password. Please try again.")
    
    def wrong_CardInfo(self):
        QtWidgets.QMessageBox.warning(self, "Wrong CardInfo", "Invalid card info. Please try again.")
    
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
