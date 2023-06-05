import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox


class PaymentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Payment Form')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        card_number_label = QLabel('Card Number:')
        self.card_number_input = QLineEdit()

        # Other payment information fields can be added here

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.process_payment)

        layout.addWidget(card_number_label)
        layout.addWidget(self.card_number_input)

        # Add other payment fields to the layout

        layout.addWidget(submit_button)

        self.setLayout(layout)

    def process_payment(self):
        card_number = self.card_number_input.text()

        # Perform payment processing logic here
        # You can add validation and connect to payment gateways or services

        QMessageBox.information(self, 'Payment Status', 'Payment processed successfully!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    payment_form = PaymentForm()
    payment_form.show()
    sys.exit(app.exec_())