from PyQt5 import QtCore, QtGui, QtWidgets



class Gifts:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class GiftsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gifts = []

        self.setWindowTitle("ParkareTo")
        self.name_label = QtWidgets.QLabel("Name:")
        self.name_entry = QtWidgets.QLineEdit()
        self.description_label = QtWidgets.QLabel("Description:")
        self.description_entry = QtWidgets.QLineEdit()
        self.price_label = QtWidgets.QLabel("Price:")
        self.price_entry = QtWidgets.QLineEdit()
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.submit_button.clicked.connect(self.add_gift)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_entry)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_entry)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def add_gift(self):
        name = self.name_entry.text()
        description = self.description_entry.text()
        price = float(self.price_entry.text())

        gift = Gifts(name, description, price)
        self.gifts.append(gift)
        QtWidgets.QMessageBox.information(self, "Gift Added", "Gift added successfully!")

        self.name_entry.clear()
        self.description_entry.clear()
        self.price_entry.clear()

    def get_gifts(self):
        if len(self.gifts) == 0:
            QtWidgets.QMessageBox.information(self, "No Gifts", "No gifts found.")
        else:
            gift_info = "Gifts:\n"
            for gift in self.gifts:
                gift_info += f"Name: {gift.name}\n"
                gift_info += f"Description: {gift.description}\n"
                gift_info += f"Price: {gift.price}\n"
                gift_info += "\n"

            QtWidgets.QMessageBox.information(self, "Gifts", gift_info)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    parkare_to = GiftsWindow()
    parkare_to.show()
    sys.exit(app.exec_())