from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Main"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.icon_url = "icons8-user-male-24.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon_url))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.ui_components()

        self.show()

    def ui_components(self):
        button = QPushButton("Click Me", self)
        # button.move(50, 50)
        button.setGeometry(QRect(100, 100, 111, 28))
        button.setIcon(QtGui.QIcon('icons8-user-male-24.png'))
        # the size doesn't go higher than the original image
        button.setIconSize(QtCore.QSize(40, 40))
        # tooltip
        button.setToolTip("click")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
