import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    print("Button cliked")

app = QApplication(sys.argv)

button = QPushButton("Clicke")
button.clicked.connect(say_hello)

#label = QLabel("<font color=red size=40>Hello World!</font>")
button.show()
app.exec()