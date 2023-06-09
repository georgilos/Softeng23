from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.setGeometry(105, 105, 405, 305)

        # Create widgets
        self.label = QtWidgets.QLabel("Enter your name:", self)
        self.label.setGeometry(QtCore.QRect(51, 51, 151, 30))
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setGeometry(QtCore.QRect(201, 50, 150, 30))
        self.button = QtWidgets.QPushButton("Submit", self)
        self.button.setGeometry(QtCore.QRect(150, 100, 100, 30))

        # Connect button click event to a function
        self.button.clicked.connect(self.submit_button_clicked)
       
       #
    def submit_button_clicked(self):
        name = self.line_edit.text()
        QtWidgets.QMessageBox.information(self, "Message", f"Hello, {name}!")

        # Clear the input field after showing the message box
        self.line_edit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())