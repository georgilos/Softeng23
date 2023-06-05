import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class SupportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Support")
        
        message_label = QLabel("Welcome to the AI Support of PARKARE TO!", self)
        message_label.move(10, 10)

        question1_label = QLabel("What is your username?", self)
        question1_label.move(10, 40)

        self.entry1 = QLineEdit(self)
        self.entry1.move(10, 70)

        question2_label = QLabel("How can I help you?", self)
        question2_label.move(10, 100)

        self.entry2 = QLineEdit(self)
        self.entry2.move(10, 131)

        submit_button = QPushButton("Submit", self)
        submit_button.move(10, 160)
        submit_button.clicked.connect(self.submit_answer)

    def submit_answer(self):
        answer1 = self.entry1.text()
        answer2 = self.entry2.text()
        QMessageBox.information(self, "AI Support", f"Hi {answer1}\nSomeone from our team will try to fix the problem: {answer2}")