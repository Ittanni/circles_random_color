from ui_file import Ui_MainWindow
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dots = []
        self.pushButton.clicked.connect(self.addDot)

    def addDot(self):
        x = random.randint(10, 400)
        y = random.randint(10, 220)
        size = random.randint(10, 200)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.dots.append((x, y, size, color))
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawDots(qp)
        qp.end()

    def drawDots(self, qp):
        for dot in self.dots:
            qp.setBrush(dot[3])
            qp.drawEllipse(dot[0], dot[1], dot[2], dot[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
