import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from math import cos, pi, sin
SCREEN_SIZE = [500, 500]


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Квадрат-объектив 2')
        self.setGeometry(500, 200, *SCREEN_SIZE)

        self.K = QLabel('K=', self)
        self.K.setGeometry(20, 5, 20, 35)

        self.k_edit = QLineEdit(self)
        self.k_edit.setGeometry(50, 8, 100, 20)

        self.N = QLabel('N=', self)
        self.N.setGeometry(200, 2, 20, 35)

        self.n_edit = QLineEdit(self)
        self.n_edit.setGeometry(250, 8, 120, 20)

        self.button = QPushButton('Рисовать', self)
        self.button.setGeometry(400, 5, 100, 35)
        self.button.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_objects(qp)
            qp.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_objects(self, qp):
        try:
            #k = int(self.k_edit.text())
            #n = float(self.n_edit.text())
            k = 0.8
            n = 2
        except ValueError:
            return
        qp.setPen(QColor(255, 0, 0))

        x_s, y_s = 100, 100
        xy = 300
        ax, ay = 0, 0
        a = 0
        for i in range(2):
            qp.drawLine(x_s, y_s, x_s + xy, y_s + a)
            qp.drawLine(x_s + xy, y_s + a, x_s + xy - a, y_s + xy + a)
            qp.drawLine(x_s + xy - a, y_s + xy + a, x_s - a, y_s + xy)
            qp.drawLine(x_s - a, y_s + xy, x_s, y_s)

            a = round(xy * (1 - k))
            x_s += a
            xy = round(xy * k)
            #y_s =


if __name__ == '__main__':
    print(cos(180))
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())




import sys
from math import cos, pi, sin

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication

SCREEN_SIZE = [500, 500]
# Задаём длину стороны и количество углов
SIDE_LENGTH = 200
SIDES_COUNT = 4


class DrawStar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('Рисуем звезду')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_star(qp)
        qp.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_star(self, qp):
        qp.setPen(QColor(255, 0, 0))
        size = 200
        coo = 1
        for g in range(6):
            nodes = []
            d = 1 * 2 * pi / 4
            print(d)
            print(cos(d), sin(d))
            circle = coo * d
            circle2 = coo * d
            x_a = int(size * cos(circle))
            y_a = int(size * sin(circle2))

            print(nodes)

            size = size * 0.8
            coo = coo * 0.8


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
















elif t == '±':
    if self.plus:
        self.label.setText(self.label.text(
        )[:len(self.label.text()) - len(self.label_2.text())])

        self.label_2.setText('-' + self.label_2.text())
        self.label.setText(self.label.text() + self.label_2.text())
        self.plus = False
    else:
        self.label.setText(self.label.text(
        )[:len(self.label.text()) - len(self.label_2.text())])

        self.label_2.setText(self.label_2.text()[1:])
        self.label.setText(self.label.text() + self.label_2.text())
        self.plus = True