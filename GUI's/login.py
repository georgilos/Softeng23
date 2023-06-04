from PyQt5 import QtCore, QtGui, QtWidgets
from signup import SignUp_Window
import pymysql as mc


class Login_Window(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(611, 418)
        LoginWindow.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(30, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(40, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password_label.setFont(font)
        self.password_label.setObjectName("pass_label")
        self.line_for_username = QtWidgets.QLineEdit(self.centralwidget)
        self.line_for_username.setGeometry(QtCore.QRect(230, 140, 181, 31))
        self.line_for_username.setObjectName("line_for_username")
        self.line_for_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_for_password.setGeometry(QtCore.QRect(230, 210, 181, 31))
        self.line_for_password.setObjectName("line_for_password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(280, 270, 93, 28))
        self.Login_Button.setObjectName("Login_Button")
        self.Register_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Register_Button.setGeometry(QtCore.QRect(290, 360, 71, 21))
        self.Register_Button.setObjectName("Register_Button")
        # self.Register_Button.clicked.connect(self.open_signup)
        self.no_account_label = QtWidgets.QLabel(self.centralwidget)
        self.no_account_label.setGeometry(QtCore.QRect(290, 330, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.no_account_label.setFont(font)
        self.no_account_label.setObjectName("no_account_label")
        
        font = QtGui.QFont()
        font.setPointSize(23)
       
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

  


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.username_label.setText(_translate("LoginWindow", "Username"))
        self.password_label.setText(_translate("LoginWindow", "Password"))
        self.label.setText(_translate("LoginWindow", "Parkare To"))
        self.Login_Button.setText(_translate("LoginWindow", "Login"))
        self.Register_Button.setText(_translate("LoginWindow", "Register"))
        self.no_account_label.setText(_translate("LoginWindow", "Don't have register yet?"))
        self.Login_Button.clicked.connect(self.login)
        
        self.Register_Button.clicked.connect(self.open_signup)
 
    
    def open_signup(self):
        self.signup = SignUp_Window()
        self.signup.show()
    
    
    
    def login(self):
     try:
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="softeng"
        )
        mycursor = mydb.cursor()

        username = self.username_line.text()
        password = self.password_line.text()

        query = "SELECT * FROM registration WHERE username = %s AND password = %s"
        value = (username, password)

        mycursor.execute(query, value)
        result = mycursor.fetchone()

        if result is not None:
            self.labelResult.setText("Login Successful")
            # Redirect to the main page or perform any other actions
        else:
            self.labelResult.setText("Invalid Credentials")

     except mc.Error as e:
        self.labelResult.setText("Error Logging In")
    


   
                                                 
# to run as python script
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Login_Window()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())


   



