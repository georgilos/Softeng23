from PyQt5 import QtCore, QtGui, QtWidgets

class Gifts(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gifts = []

        self.setWindowTitle("Gifts")
        self.show_gift_details_button = QtWidgets.QPushButton("Show Gift Details")
        self.show_gift_details_button.clicked.connect(self.showGiftDetails)

        self.available_gifts_button = QtWidgets.QPushButton("Available Gifts")
        self.available_gifts_button.clicked.connect(self.availableGifts)

        self.gift_selection_button = QtWidgets.QPushButton("Gift Selection")
        self.gift_selection_button.clicked.connect(self.giftSelection)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.show_gift_details_button)
        layout.addWidget(self.available_gifts_button)
        layout.addWidget(self.gift_selection_button)
        self.setLayout(layout)

    def showGiftDetails(self):
        if len(self.gifts) == 0:
            QtWidgets.QMessageBox.information(self, "No Gifts", "No gifts found.")
        else:
            gift_info = "Gifts:\n"
            for gift in self.gifts:
                gift_info += f"Name: {gift.name}\n"
                gift_info += f"Description: {gift.description}\n"
                gift_info += f"Price: {gift.price}\n"
                gift_info += "\n"

            QtWidgets.QMessageBox.information(self, "Gift Details", gift_info)

    def availableGifts(self):
        if len(self.gifts) == 0:
            QtWidgets.QMessageBox.information(self, "No Gifts", "No gifts found.")
        else:
            available_gifts = "Available Gifts:\n"
            for i, gift in enumerate(self.gifts, 1):
                available_gifts += f"{i}. {gift.name}\n"

            QtWidgets.QMessageBox.information(self, "Available Gifts", available_gifts)

    def giftSelection(self):
        if len(self.gifts) == 0:
            QtWidgets.QMessageBox.information(self, "No Gifts", "No gifts found.")
        else:
            # Prompt the user to select gifts
            selected_gift, ok = QtWidgets.QInputDialog.getItem(
                self,
                "Gift Selection",
                "Select a gift:",
                [gift.name for gift in self.gifts],
                editable=False
            )

            if ok:
                selected_gift_info = ""
                for gift in self.gifts:
                    if gift.name == selected_gift:
                        selected_gift_info += f"Name: {gift.name}\n"
                        selected_gift_info += f"Description: {gift.description}\n"
                        selected_gift_info += f"Price: {gift.price}\n"
                        selected_gift_info += "\n"

                QtWidgets.QMessageBox.information(self, "Selected Gift", selected_gift_info)

    #valid selection function
    def validSelection(self):
        QtWidgets.QMessageBox.information(self, "Valid Selection")

    #invalid selection function
    def validSelection(self):
        QtWidgets.QMessageBox.information(self, "Invalid Selection")

    #add points function
    def addPoints(self):
          QtWidgets.QMessageBox.information(self, "Your Points will be added!")

    #avaliable points function
    def isAvailablePoints(self):
          QtWidgets.QMessageBox.information(self, "Your Points are  available!")    
    #notAvaliablePoints function
    def notAvailablePoints(self):
          QtWidgets.QMessageBox.information(self, "Your Points are not available!")

# Example usage
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    gifts_window = Gifts()

    # Create some gift objects
    # gift1 = Gifts("Gift 1", "Description 1", 10.99)
    # gift2 = Gifts("Gift 2", "Description 2", 19.99)
    # gift3 = Gifts("Gift 3", "Description 3", 5.99)

    # # Add the gifts to the Gifts window
    # gifts_window.gifts.extend([gift1, gift2, gift3])

    gifts_window.show()

    sys.exit(app.exec_())
