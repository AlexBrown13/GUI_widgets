import sys
from PySide6.QtWidgets import (QApplication, QDialog, 
        QLineEdit, QPushButton, QVBoxLayout, QTextEdit,
        QLabel
    )
from PySide6.QtCore import QThread, Signal
from chat import chat_service


class TaskThread(QThread):
    finished = Signal(str)

    def __init__(self, question):
        super().__init__()
        self.question = question

    def run(self):
        response = chat_service(self.question)
        self.finished.emit(response)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("AI Asistant Tool")

        self.label_title = QLabel("Chat with Ollama AI")
        self.edit = QLineEdit("")
        self.button = QPushButton("Ask")
        self.text = QTextEdit("")
        self.text.setReadOnly(True)

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
        question = self.edit.text().strip()

        if not question:
            self.text.append("Please enter a question\n")
            return None
        
        self.edit.clear()

        self.text.append(f"You: {question}")
        self.text.append("AI: Thinking...\n")

        self.task = TaskThread(question)

        self.task.finished.connect(self.show_response)
        self.task.start()


    def show_response(self, response):
        self.text.append(f"AI: {response}")
        self.text.append("-" * 40)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.resize(600,500)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())