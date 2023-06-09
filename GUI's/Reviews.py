from PyQt5 import QtCore, QtGui, QtWidgets

class ReviewsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reviews")
        self.setGeometry(100, 100, 400, 300)

        self.reviews = []  # List to store the reviews

   
        main_layout = QtWidgets.QVBoxLayout()
        label_review = QtWidgets.QLabel("Enter Review:")
        main_layout.addWidget(label_review)
        self.input_review = QtWidgets.QLineEdit()
        main_layout.addWidget(self.input_review)
        label_stars = QtWidgets.QLabel("Enter Stars: ")
        main_layout.addWidget(label_stars)
        self.input_stars = QtWidgets.QLineEdit()
        main_layout.addWidget(self.input_stars)
        btn_submit = QtWidgets.QPushButton("Submit Review")
        btn_submit.clicked.connect(self.submitReview)
        btn_choose_stars = QtWidgets.QPushButton("Submit Stars")
        btn_choose_stars.clicked.connect(self.chooseStars)
        btn_upload = QtWidgets.QPushButton("Upload")
        btn_upload.clicked.connect(self.uplooad)
        main_layout.addWidget(btn_submit)
        main_layout.addWidget(btn_choose_stars)
        
        self.list_reviews = QtWidgets.QListWidget()
        main_layout.addWidget(self.list_reviews)
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        main_layout.addWidget(btn_upload)

    def submitReview(self):
        # Function to handle review submission
        review_text = self.input_review.text()

        if review_text:
            # Add the review to the list
            self.reviews.append(review_text)

            # Clear the input field
            self.input_review.clear()

            # Update the list widget to display the reviews
            self.updateReviewList()
        else:
            self.incompletereview()

    def updateReviewList(self):
        # Function to update the list widget with the submitted reviews
        self.list_reviews.clear()
        self.list_reviews.addItems(self.reviews)

    def incompletereview(self):
        # Function to display a message box with a warning for incomplete review
        QtWidgets.QMessageBox.warning(self, "Incomplete Review", "Please enter a review before submitting.")

    
    def chooseStars(self):
        # Function to display a message box with a warning for incomplete review
        QtWidgets.QMessageBox.warning(self, "Enter stars", "Please enter the stars before submitt your reviews.")

    def uplooad(self):
        # Function to display a message box with a message for upload the review
        QtWidgets.QMessageBox.warning(self, "Your review has been uploaded to the system!")

    def confirmation(self):
        # Function to display a message box for the confirmation
        QtWidgets.QMessageBox.warning(self, "Confirm this review")

    def writereview(self):
        # Function to open a dialog for writing a review
        review_text, ok = QtWidgets.QInputDialog.getText(self, "Write Review", "Enter your review:")

        if ok and review_text:
            # Add the review to the list
            self.reviews.append(review_text)

            # Update the list widget to display the reviews
            self.updateReviewList()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reviews_window = ReviewsWindow()
    reviews_window.show()
    sys.exit(app.exec_())
