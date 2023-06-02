from PyQt5 import QtCore, QtGui, QtWidgets
# from signup import Ui_MainWindow
import mysql.connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 418)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.Register_Button.clicked.connect(self.open_signup)

    
        self.no_account_label = QtWidgets.QLabel(self.centralwidget)
        self.no_account_label.setGeometry(QtCore.QRect(290, 330, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.no_account_label.setFont(font)
        self.no_account_label.setObjectName("no_account_label")
        
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
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Parkare To"))
        self.Login_Button.setText(_translate("MainWindow", "Login"))
        self.Register_Button.setText(_translate("MainWindow", "Register"))
        
        self.no_account_label.setText(_translate("MainWindow", "Don't have register yet?"))
        self.Login_Button.clicked.connect(self.login)

    def login(self):
        username = self.line_for_username.text()
        password = self.line_for_pass.text()


    def open_signup(self):
        self.signup =  Ui_MainWindow()
        self.signup.show()
                                                 
# to run as python script
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


   



