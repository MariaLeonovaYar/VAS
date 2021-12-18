import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

if __name__ == "__main__":

    # Создание окна
    app = QApplication(sys.argv)

    # Контейнер, содержащий все виджеты
    win = QMainWindow()

    # Размер окна x, y, длина, ширина
    win.setGeometry(400, 400, 400, 300)

    # Заголовок окна
    win.setWindowTitle("Системы векторного сложения (VAS)")

    # Label Text
    initial_label = QLabel(win)
    initial_label.setText("Введите координаты начального вектора")
    initial_label.move(10, 10)
 
    # Окно для ввода начального вектора
    initial_v = QtWidgets.QLineEdit(win)
    initial_v.move(10, 40)
    initial_v.resize(180, 40)


    # Отобразить все
    win.show()
    # Окно не закроется без нажатия на кнопку с крестиком
    sys.exit(app.exec_())
