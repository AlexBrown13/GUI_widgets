import sys
from PySide6.QtWidgets import (QApplication, QDialog, 
        QLineEdit, QPushButton, QVBoxLayout, QTextEdit)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("AI Asistant Tool")

        self.edit = QLineEdit("")
        self.button = QPushButton("Show Greeting")
        self.text = QTextEdit("")

        # Create layout and add widget
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.text)
        # Set dialog layout
        self.setLayout(layout)

        self.button.clicked.connect(self.greetings)


    def greetings(self):
        self.text.setText(self.edit.text())



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.resize(600,500)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())