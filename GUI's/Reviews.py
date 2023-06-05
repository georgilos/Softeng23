from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Review(object):
    def setupUi(self, Review):
        Review.setObjectName("Review")
        Review.resize(560, 600)
        Review.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(Review)
        self.centralwidget.setObjectName("centralwidget")
        self.review_label = QtWidgets.QLabel(self.centralwidget)
        self.review_label.setGeometry(QtCore.QRect(220, 40, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.review_label.setFont(font)
        self.review_label.setObjectName("review_label")
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setGeometry(QtCore.QRect(450, 50, 90, 65))  # Adjust the width and height values
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
        self.helpButton.setText(_translate("Review", "Help"))
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


class ReviewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Review")
        self.setGeometry(100, 100, 400, 300)

        self.ui = Ui_Review()
        self.ui.setupUi(self)

        self.reviews = []  # List to store the reviews

        # Connect button signals to functions
        self.ui.helpButton.clicked.connect(self.showHelp)
        self.ui.submitButton.clicked.connect(self.submitReview)
        self.ui.cancelButton.clicked.connect(self.close)

    def showHelp(self):
        # Function to show help information
        QtWidgets.QMessageBox.information(self, "Help", "Help information goes here.")

    def submitReview(self):
        # Function to handle review submission
        username = "Alexis tsampas  "  # Replace with the actual username
        rating = 5  # Replace with the actual rating value
        comment = "This is a great app!"  # Replace with the actual comment

        review = Review(username, rating, comment)
        self.reviews.append(review)

        # Do something with the submitted review data (e.g., store in a database)

        # Show a message box to indicate successful submission
        QtWidgets.QMessageBox.information(self, "Success", "Review submitted successfully.")

        # Clear the input fields
        # self.ui.usernameLineEdit.clear()
        # self.ui.ratingSpinBox.setValue(0)
        # self.ui.commentTextEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reviewWindow = ReviewWindow()
    reviewWindow.show()
    sys.exit(app.exec_())