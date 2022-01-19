import sys
from calc import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QApplication


class Calculator(QMainWindow, Ui_Form):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle('Калькулятор 2')
        self.setupUi(self)

        self.symb_string = ''
        self.dot_pressed = False

        for button in self.buttonGroup_digits.buttons():
            button.clicked.connect(self.digit)

        for button in self.buttonGroup_binary.buttons():
            button.clicked.connect(self.digit)

        self.btn_clear.clicked.connect(self.digit)
        self.btn_eq.clicked.connect(self.digit)
        self.btn_dot.clicked.connect(self.digit)
        self.btn_fact.clicked.connect(self.digit)
        self.btn_sqrt.clicked.connect(self.digit)

    def digit(self):
        if self.table.value() == 'error':
            self.table.display(0)

        button = self.sender()
        t = button.text()

        if button in self.buttonGroup_digits.buttons():
            if self.symb_string:
                if str(self.table.value()) == self.symb_string[:len(str(self.table.value()))]:
                    self.table.display(0)
                if self.dot_pressed:
                    self.symb_string += '.' + t
                else:
                    self.symb_string += t

            if self.dot_pressed:
                self.table.display(self.table.value() + 0.1 * float(t))
            else:
                self.table.display(10 * self.table.value() + float(t))
        elif button in self.buttonGroup_binary.buttons() or t == '!' or t == '√':
            if t == '^':
                self.symb_string += f'{self.table.value()} ** '
                self.dot_pressed = False
            elif t == '!':
                try:
                    ans = 1
                    for i in range(1, int(self.table.value()) + 1):
                        ans *= i
                    self.table.display(ans)
                except OverflowError:
                    self.table.display('error')
                self.symb_string = ''
                self.dot_pressed = False
            elif t == '√':
                try:
                    ans = self.table.value() ** 0.5
                    self.table.display(ans)
                except TypeError:
                    self.table.display('error')
                self.symb_string = ''
                self.dot_pressed = False
            else:
                self.symb_string += f'{self.table.value()} {t}'
                self.dot_pressed = False
        elif t == '.':
            self.dot_pressed = True
        elif t == 'С':
            self.table.display(0)
            self.symb_string = ''
            self.dot_pressed = False
        elif t == '=':
            if self.symb_string:
                try:
                    self.table.display(eval(self.symb_string))
                except ZeroDivisionError:
                    self.table.display('error')
                except SyntaxError:
                    self.table.display('error')
            self.symb_string = ''
            self.dot_pressed = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())