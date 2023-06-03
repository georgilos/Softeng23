from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Review(object):
    def setupUi(self, Review):
        Review.setObjectName("Review")
        Review.resize(560, 600)
        Review.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(Review)
        self.centralwidget.setObjectName("centralwidget")
        self.review_label = QtWidgets.QLabel(self.centralwidget)
        self.review_label.setGeometry(QtCore.QRect(190, 40, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.review_label.setFont(font)
        self.review_label.setObjectName("review_label")
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setGeometry(QtCore.QRect(480, 50, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.helpButton.setFont(font)
        self.helpButton.setObjectName("helpButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(210, 230, 139, 176))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.submitButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.gridLayout.addWidget(self.submitButton, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        Review.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Review)
        self.statusbar.setObjectName("statusbar")
        Review.setStatusBar(self.statusbar)

        self.retranslateUi(Review)
        QtCore.QMetaObject.connectSlotsByName(Review)

    def retranslateUi(self, Review):
        _translate = QtCore.QCoreApplication.translate
        Review.setWindowTitle(_translate("Review", "MainWindow"))
        self.review_label.setText(_translate("Review", "Review"))
        self.helpButton.setText(_translate("Review", "!"))
        self.submitButton.setText(_translate("Review", "Submit"))
        self.cancelButton.setText(_translate("Review", "Cancel"))


class Review:
    def __init__(self, username, rating, comment):
        self.username = username
        self.rating = rating
        self.comment = comment


class ParkingApp:
    def __init__(self, name):
        self.name = name

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Review()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())