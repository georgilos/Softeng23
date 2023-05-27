

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_checkout(object):
    def setupUi(self, checkout):
        checkout.setObjectName("checkout")
        checkout.resize(560, 600)
        checkout.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(checkout)
        self.centralwidget.setObjectName("centralwidget")
        self.checkout_label = QtWidgets.QLabel(self.centralwidget)
        self.checkout_label.setGeometry(QtCore.QRect(190, 40, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.checkout_label.setFont(font)
        self.checkout_label.setObjectName("checkout_label")
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
        self.checkoutButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkoutButton.setFont(font)
        self.checkoutButton.setObjectName("checkoutButton")
        self.gridLayout.addWidget(self.checkoutButton, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.problemButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.problemButton.setFont(font)
        self.problemButton.setObjectName("problemButton")
        self.gridLayout.addWidget(self.problemButton, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        checkout.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(checkout)
        self.statusbar.setObjectName("statusbar")
        checkout.setStatusBar(self.statusbar)

        self.retranslateUi(checkout)
        QtCore.QMetaObject.connectSlotsByName(checkout)

    def retranslateUi(self, checkout):
        _translate = QtCore.QCoreApplication.translate
        checkout.setWindowTitle(_translate("checkout", "MainWindow"))
        self.checkout_label.setText(_translate("checkout", "Check-out"))
        self.helpButton.setText(_translate("checkout", "!"))
        self.checkoutButton.setText(_translate("checkout", "Checkout"))
        self.problemButton.setText(_translate("checkout", "Problem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    checkout = QtWidgets.QMainWindow()
    ui = Ui_checkout()
    ui.setupUi(checkout)
    checkout.show()
    sys.exit(app.exec_())
