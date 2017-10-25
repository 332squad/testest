import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setToolTip('This is a <b>QWidget</b> widget')
        btn1 = QPushButton('Категория1', self)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 350)
        btn2 = QPushButton('Категория2', self)
        btn2.resize(btn2.sizeHint())
        btn2.move(150, 350)
        btn3 = QPushButton('Категория3', self)
        btn3.resize(btn3.sizeHint())
        btn3.move(250, 350)
        btn4 = QPushButton('Категория4', self)
        btn4.resize(btn4.sizeHint())
        btn4.move(350, 350)
        btn5 = QPushButton('Категория5', self)
        btn5.resize(btn5.sizeHint())
        btn5.move(450, 350)

        btn1.clicked.connect(self.button1Clicked)
        btn2.clicked.connect(self.button2Clicked)
        btn3.clicked.connect(self.button3Clicked)
        btn4.clicked.connect(self.button4Clicked)
        btn5.clicked.connect(self.button5Clicked)

        self.setGeometry(300, 300, 580, 400)
        self.setWindowTitle('Learning')
        self.show()

    def button1Clicked(self):
        print("1")

    def button2Clicked(self):
        print("2")

    def button3Clicked(self):
        print("3")

    def button4Clicked(self):
        print("4")

    def button5Clicked(self):
        print("5")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())