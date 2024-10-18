from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt, QTimer
import random as rnd
import sys


class Game21(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('21')
        self.setFixedSize(700, 500)
        self.move(500, 0)
        self.setStyleSheet("background-color: green;")
        self.timer = QTimer()

        self.start()


    def start(self):
        self.start_button = None
        self.add = None
        self.end = False
        self.win = False
        self.draw = False

        self.gamer_count = 0
        self.d_count = 0

        self.gamer_count_label = None
        self.d_count_label = None

        self.x_gamer = 15
        self.y_gamer = 260
        self.x_d = 15
        self.y_d = 180

        self.create_game_count()

        self.start_button = QPushButton('Начать', self)

        self.start_button.clicked.connect(self.on_click_start)
        self.start_button.setStyleSheet("""
                                border-radius: 10px;
                                font-size: 20px;
                                color: #FFFFFF;
                                background-color: #A9A9A9;
                                """)
        self.start_button.setGeometry(305, 420, 90, 50)
        self.start_button.show()

    def on_click_start(self):
        self.add_number_gamer()
        self.start_button.deleteLater()

        self.add = QPushButton('Ещё', self)
        self.add.clicked.connect(self.add_number_gamer)
        self.add.setStyleSheet("""
                                        border-radius: 10px;
                                        font-size: 20px;
                                        color: #FFFFFF;
                                        background-color: #A9A9A9;
                                        """)
        self.add.setGeometry(200, 420, 100, 50)
        self.add.show()

        self.stop = QPushButton('Стоп', self)
        self.stop.clicked.connect(self.on_click_stop)
        self.stop.setStyleSheet("""
                                border-radius: 10px;
                                font-size: 20px;
                                color: #FFFFFF;
                                background-color: #A9A9A9;
                                """)
        self.stop.setGeometry(330, 420, 100, 50)
        self.stop.show()

    def on_click_stop(self):
        self.end = True
        while self.d_count <= 17:
            self.add_number_d()

        if self.gamer_count > self.d_count:
            self.win = True
        elif self.gamer_count == self.d_count:
            self.draw = True

        self.timer.timeout.connect(self.show_result)
        self.timer.start(900)

    def add_number_d(self):
        num = rnd.randint(1, 11)

        label = QLabel(str(num), self)
        label.setGeometry(self.x_d, self.y_d, 50, 50)
        label.setStyleSheet("""
                                border: 2px solid #000000;
                                border-radius: 10px;
                                font-size: 25px;
                                color: #FFFFFF;
                                """)
        label.setAlignment(Qt.AlignCenter)
        label.show()

        self.x_d += 62
        if self.x_d == 697:
            self.x_d = 15
            self.y_d -= 65

        self.d_count += num
        self.d_count_label.setText(str(self.d_count))
        self.d_count_label.update()

        if self.d_count > 21:
            self.win = True

    def create_game_count(self):
        self.gamer_count_label = QLabel(str(self.gamer_count), self)
        self.gamer_count_label.setGeometry(580, 380, 100, 100)
        self.gamer_count_label.setStyleSheet("""
                            border: 2px solid #000000;
                            border-radius: 10px;
                            font-size: 40px;
                            color: #FFFFFF;
                            """)
        self.gamer_count_label.setAlignment(Qt.AlignCenter)
        self.gamer_count_label.show()

        self.d_count_label = QLabel(str(self.d_count), self)
        self.d_count_label.setGeometry(580, 20, 100, 100)
        self.d_count_label.setStyleSheet("""
                            border: 2px solid #000000;
                            border-radius: 10px;
                            font-size: 40px;
                            color: #FFFFFF;
                            """)
        self.d_count_label.setAlignment(Qt.AlignCenter)
        self.d_count_label.show()

    def add_number_gamer(self):
        if not self.end:
            num = rnd.randint(1, 11)

            label = QLabel(str(num), self)
            label.setGeometry(self.x_gamer, self.y_gamer, 50, 50)
            label.setStyleSheet("""
                                    border: 2px solid #000000;
                                    border-radius: 10px;
                                    font-size: 25px;
                                    color: #FFFFFF;
                                    """)
            label.setAlignment(Qt.AlignCenter)
            label.show()

            self.x_gamer += 62
            if self.x_gamer == 697:
                self.x_gamer = 15
                self.y_gamer += 65

            self.gamer_count += num
            self.gamer_count_label.setText(str(self.gamer_count))
            self.gamer_count_label.update()

            if self.gamer_count >= 21:
                self.end = True
                if self.gamer_count == 21:
                    self.win = True
                self.show_result()

    def show_result(self):
        self.timer.stop()
        frame = QFrame(self)
        frame.setGeometry(0, 0, 700, 500)
        frame.setStyleSheet('background-color: rgba(0, 0, 0, 0.5);')
        frame.show()

        if self.draw:
            result = 'НИЧЬЯ'
            color = '#FFFFFF'
        else:
            result = 'ПРОИГРЫШ'
            color = '#FF0000'
            if self.win:
                result = 'ПОБЕДА'
                color = '#00FF00'

        label = QLabel(result, self)
        label.setGeometry(225, 190, 250, 50)
        label.setStyleSheet(f"""
                                    border: 2px solid #FFFF00;
                                    border-radius: 10px;
                                    font-size: 20px;
                                    color: {color};
                                    background-color: #000000;
                                    """)
        label.setAlignment(Qt.AlignCenter)
        label.show()

        button = QPushButton('Продолжить', self)
        button.clicked.connect(self.nex_level)
        button.setStyleSheet("""
                                        border: 2px solid #A9A9A9;
                                        border-radius: 10px;
                                        font-size: 20px;
                                        color: #FFFFFF;
                                        background-color: #000000;
                                        """)
        button.setGeometry(225, 260, 250, 50)
        button.show()

    def nex_level(self):
        for widget in self.findChildren(QWidget):
            widget.deleteLater()

        self.update()
        self.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('icon.png'))

    main_window = Game21()
    main_window.show()

    sys.exit(app.exec_())