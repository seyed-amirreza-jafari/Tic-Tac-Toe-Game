from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMenu
from PyQt5 import uic
import sys

class UI(QMainWindow):
    counter = 0
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('Tic_Tac_Toe_Game.ui', self)

        self.square_1 = self.findChild(QPushButton, 'Square_1')
        self.square_2 = self.findChild(QPushButton, 'Square_2')
        self.square_3 = self.findChild(QPushButton, 'Square_3')
        self.square_4 = self.findChild(QPushButton, 'Square_4')
        self.square_5 = self.findChild(QPushButton, 'Square_5')
        self.square_6 = self.findChild(QPushButton, 'Square_6')
        self.square_7 = self.findChild(QPushButton, 'Square_7')
        self.square_8 = self.findChild(QPushButton, 'Square_8')
        self.square_9 = self.findChild(QPushButton, 'Square_9')
        self.turn = self.findChild(QLabel, 'Whose_Turn_Is')
        self.New_Game.triggered.connect(self.reset)

        self.squares = [
            self.square_1,
            self.square_2,
            self.square_3,
            self.square_4,
            self.square_5,
            self.square_6,
            self.square_7,
            self.square_8,
            self.square_9]

        for square in self.squares:
            square.setText('')
            square.setEnabled(True)
            square.setStyleSheet('QPushButton {color: black;}')

        self.square_1.clicked.connect(lambda: self.square_clicked(self.square_1))
        self.square_2.clicked.connect(lambda: self.square_clicked(self.square_2))
        self.square_3.clicked.connect(lambda: self.square_clicked(self.square_3))
        self.square_4.clicked.connect(lambda: self.square_clicked(self.square_4))
        self.square_5.clicked.connect(lambda: self.square_clicked(self.square_5))
        self.square_6.clicked.connect(lambda: self.square_clicked(self.square_6))
        self.square_7.clicked.connect(lambda: self.square_clicked(self.square_7))
        self.square_8.clicked.connect(lambda: self.square_clicked(self.square_8))
        self.square_9.clicked.connect(lambda: self.square_clicked(self.square_9))

        self.show()

    def square_clicked(self, square_number):
        if UI.counter % 2 == 0:
            square_number.setText('X')
            self.turn.setText('O turn')
        else:
            square_number.setText('O')
            self.turn.setText('X turn')

        square_number.setEnabled(False)

        UI.counter += 1

        self.check_win()

    def win(self, square_A, square_B, square_C):
        if square_A.text() == 'X':
            self.turn.setText('X wins! Start a new game!')
        if square_A.text() == 'O':
            self.turn.setText('O wins! Start a new game!')

        square_A.setStyleSheet('QPushButton {color: green;}')
        square_B.setStyleSheet('QPushButton {color: green;}')
        square_C.setStyleSheet('QPushButton {color: green;}')

        self.squares = [
            self.square_1,
            self.square_2,
            self.square_3,
            self.square_4,
            self.square_5,
            self.square_6,
            self.square_7,
            self.square_8,
            self.square_9]
        
        for square in self.squares:
            square.setEnabled(False)

    def check_win(self):
        if self.square_1.text() != '' and self.square_1.text() == self.square_2.text() == self.square_3.text():
            self.win(self.square_1, self.square_2, self.square_3)
        elif self.square_4.text() != '' and self.square_4.text() == self.square_5.text() == self.square_6.text():
            self.win(self.square_4, self.square_5, self.square_6)
        elif self.square_7.text() != '' and self.square_7.text() == self.square_8.text() == self.square_9.text():
            self.win(self.square_7, self.square_8, self.square_9)
        elif self.square_1.text() != '' and self.square_1.text() == self.square_4.text() == self.square_7.text():
            self.win(self.square_1, self.square_4, self.square_7)
        elif self.square_2.text() != '' and self.square_2.text() == self.square_5.text() == self.square_8.text():
            self.win(self.square_2, self.square_5, self.square_8)
        elif self.square_3.text() != '' and self.square_3.text() == self.square_6.text() == self.square_9.text():
            self.win(self.square_3, self.square_6, self.square_9)
        elif self.square_1.text() != '' and self.square_1.text() == self.square_5.text() == self.square_9.text():
            self.win(self.square_1, self.square_5, self.square_9)
        elif self.square_3.text() != '' and self.square_3.text() == self.square_5.text() == self.square_7.text():
            self.win(self.square_3, self.square_5, self.square_7)

    def reset(self):
        self.squares = [
            self.square_1,
            self.square_2,
            self.square_3,
            self.square_4,
            self.square_5,
            self.square_6,
            self.square_7,
            self.square_8,
            self.square_9]
        
        for square in self.squares:
            square.setText('')
            square.setEnabled(True)
            square.setStyleSheet('QPushButton {color: black;}')
        
        self.turn.setText('X turn')

        UI.counter = 0

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
