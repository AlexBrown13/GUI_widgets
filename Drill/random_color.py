import sys, random
from PySide6 import QtCore, QtWidgets, QtGui

class ColorWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.color = ["Red", "Green", 'Blue']

        self.button = QtWidgets.QPushButton("Get color")
        self.text = QtWidgets.QLabel("Color", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.print_color)

    @QtCore.Slot()
    def print_color(self):
        self.text.setText(random.choice(self.color))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ColorWidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())


