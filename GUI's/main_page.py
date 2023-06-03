from PyQt5 import QtCore, QtGui, QtWidgets
from parking_search import ParkingWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 566)
        MainWindow.setStyleSheet("background-color: lightblue;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 40, 367, 450))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setAlignment(QtCore.Qt.AlignHCenter)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.parking_search_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        self.parking_search_button.setStyleSheet("background-color: lightcyan;")
        font.setPointSize(11)
        self.parking_search_button.setFont(font)
        self.parking_search_button.setObjectName("parking_search_button")
        self.gridLayout.addWidget(self.parking_search_button, 2, 2, 10, 20)
        self.parking_search_button.setSizePolicy(sizePolicy)

        self.reservation_history_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reservation_history_button.setFont(font)
        self.reservation_history_button.setObjectName("reservation_history_button")
        self.gridLayout.addWidget(self.reservation_history_button, 4, 2, 10, 20)
        self.reservation_history_button.setSizePolicy(sizePolicy)

        self.change_user_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.change_user_button.setFont(font)
        self.change_user_button.setObjectName("change_user_button")
        self.gridLayout.addWidget(self.change_user_button, 6, 2, 10, 20)
        self.change_user_button.setSizePolicy(sizePolicy)

        self.gifts_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gifts_button.setFont(font)
        self.gifts_button.setObjectName("gifts_button")
        self.gridLayout.addWidget(self.gifts_button, 8, 2, 10, 20)
        self.gifts_button.setSizePolicy(sizePolicy)

        self.Reviews_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        self.Reviews_button.setStyleSheet("background-color: lightcyan;")
        font.setPointSize(11)
        self.Reviews_button.setFont(font)
        self.Reviews_button.setObjectName("Reviews_button")
        self.gridLayout.addWidget(self.Reviews_button, 10, 2, 10, 20)
        self.Reviews_button.setSizePolicy(sizePolicy)

        self.user_support_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_support_button.setFont(font)
        self.user_support_button.setObjectName("user_support_button")
        self.gridLayout.addWidget(self.user_support_button, 12, 2, 10, 20)
        self.user_support_button.setSizePolicy(sizePolicy)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.homepage_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.homepage_label.setFont(font)
        self.homepage_label.setObjectName("homepage_label")
        self.gridLayout.addWidget(self.homepage_label, 0, 1, 1, 3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parking_search_button.setText(_translate("MainWindow", "Parking Search"))
        self.reservation_history_button.setText(_translate("MainWindow", "Reservation History"))
        self.change_user_button.setText(_translate("MainWindow", "Change User Details"))
        self.gifts_button.setText(_translate("MainWindow", "Gifts"))     
        self.Reviews_button.setText(_translate("MainWindow", "Reviews"))
        self.homepage_label.setText(_translate("MainWindow", "Homepage"))
        self.user_support_button.setText(_translate("MainWindow", "User Support"))

        self.parking_search_button.clicked.connect(self.open_parking_search)

    def open_parking_search(self):
        self.parking_search = ParkingWindow()
        self.parking_search.show()


if __name__ == "__main__":
    import sys
    import os

    # Prevent bytecode generation
    sys.dont_write_bytecode = True
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
