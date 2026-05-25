import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        dial = QDial()
        dial.setRange(0, 100)
        dial.setSingleStep(1)

        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.dial_position)
        dial.sliderPressed.connect(self.dial_pressed)
        dial.sliderReleased.connect(self.dial_released)

        self.setCentralWidget(dial)

    def value_changed(self, value):
        print(value)

    def dial_position(self, position):
        print("position", position)

    def dial_pressed(self):
        print("Pressed!")

    def dial_released(self):
        print("Released")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()