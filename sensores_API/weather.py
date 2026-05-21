import sys
import time

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QTextEdit,
    QVBoxLayout
)

from PySide6.QtCore import (
    QThread,
    Signal
)


class Worker(QThread):

    finished = Signal(str)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):

        time.sleep(5)

        result = f"response weather climate {self.name}"
        self.finished.emit(result)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather")

        self.button = QPushButton("Start task")

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        layout = QVBoxLayout()

        layout.addWidget(self.button)
        layout.addWidget(self.text)

        self.setLayout(layout)

        self.button.clicked.connect(
            self.start_task
        )

        # Keep thread references alive
        self.workers = []

    def start_task(self):

        for i in range(3):
            worker = Worker(f"worker {i}")

            worker.finished.connect(
                self.show_result
            )
            worker.finished.connect(
                worker.deleteLater
            )

            self.workers.append(worker)

            worker.start()


    def show_result(self, message):

        print(f"message: {message}")
        self.text.append(message)


app = QApplication(sys.argv)
window = Window()
window.resize(400, 300)
window.show()

sys.exit(app.exec())