import sys

from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Untitled.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        x = int(randint(25, 200))
        qp.drawEllipse(int(randint(150, 400)), int(randint(150, 400)), x, x)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
