import sys
from PySide6.QtWidgets import (QApplication, QDialog, 
        QLineEdit, QPushButton, QVBoxLayout, QTextEdit,
        QLabel
    )
from chat import chat_service


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("AI Asistant Tool")

        self.label_title = QLabel("Chat with Ollama AI")
        self.edit = QLineEdit("")
        self.button = QPushButton("Ask")
        self.text = QTextEdit("")

        # Create layout and add widget
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.text)
        # Set dialog layout
        self.setLayout(layout)

        self.button.clicked.connect(self.ask_ai)


    def ask_ai(self):
        question = self.edit.text()

        if not question:
            self.text.setText("Please enter a question")
            return None
        
        #TODO add processEvents
        # self.text.setText("Thinking...")

        response = chat_service(question)
        self.text.setText(response)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.resize(600,500)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())