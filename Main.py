#!/usr/bin/env python3
# coding=utf-8

# Программа создает графический интерфейс с таблицей (2 столбца, 10 строк).
# Первый столбец заполняется случайными числами, во втором вычисляются значения
# по формуле: Y_i = \frac{\sqrt[3]{(\sum K_i)^2} * [\sin^2(K_i) - \cos^2(K_{i-1})]^3}{\prod K_{i-1}}, i = 1..10
# где:
# - \sum K_i: сумма всех элементов от K(0) до K(i) включительно
# - \prod K_{i-1}: произведение всех элементов от K(0) до K(i-1)
# - \sin^2(K_i) - \cos^2(K_{i-1}): разность квадратов синуса текущего и косинуса предыдущего элемента
# Вычисления начинаются с i = 1, для i = 0 устанавливается значение 'none'

import sys  # Для работы с системными функциями (передача аргументов командной строки)
from PyQt5 import QtGui  # Для работы с иконками и изображениями
from PyQt5.QtGui import QPixmap  # Для загрузки и отображения изображений
from PyQt5.QtWidgets import *  # Для создания интерфейса (QDialog, QTableWidgetItem и др.)
from PyQt5.uic import loadUi  # Для загрузки UI-файла
from calculator import Calculator  # Импортируем класс Calculator
from random import randint  # Для генерации случайных чисел (добавлен импорт для randint)

def fill_random_numbers(table_widget):
    """
    Заполняет первый столбец таблицы случайными числами от 0 до 101.
    :param table_widget: Виджет таблицы, в которую записываются числа
    """
    i = 0  # Индекс текущей строки
    # Проходим по всем строкам таблицы (0 до 9, всего 10 строк)
    while i < table_widget.rowCount():
        random_num = randint(0, 101)  # Генерируем случайное число в диапазоне 0-101
        # Записываем число в первый столбец (столбец 0) текущей строки
        table_widget.setItem(i, 0, QTableWidgetItem(str(random_num)))
        i += 1  # Переходим к следующей строке

def clear(table_widget):
    """
    Очищает содержимое таблицы.
    :param table_widget: Виджет таблицы, который нужно очистить
    """
    # Удаляем все данные из таблицы, сохраняя структуру (заголовки и размеры)
    table_widget.clearContents()

def main():
    """
    Основная функция программы: создает и настраивает интерфейс, подключает кнопки.
    """
    # Создаем приложение PyQt5
    app = QApplication(sys.argv)
    # Создаем диалоговое окно
    window = QDialog()
    # Загружаем интерфейс из UI-файла
    loadUi('uis/main.ui', window)

    # Настраиваем заголовок окна
    window.setWindowTitle('Сложные табличные вычисления в Python')
    # Устанавливаем иконку окна
    window.setWindowIcon(QtGui.QIcon('images/logo.png'))
    # Устанавливаем изображение задачи и масштабируем его
    window.label_img.setPixmap(QPixmap('images/task.png'))
    window.label_img.setScaledContents(True)

    # Создаем экземпляр класса Calculator
    calculator = Calculator()

    # Подключаем кнопки к соответствующим функциям с использованием lambda для передачи параметров
    window.btn_random_number.clicked.connect(lambda: fill_random_numbers(window.tableWidget))
    window.btn_solve.clicked.connect(lambda: calculator.calculate(window.tableWidget))
    window.btn_clear.clicked.connect(lambda: clear(window.tableWidget))
    window.btn_exit.clicked.connect(window.close)

    # Показываем окно на экране
    window.show()
    # Запускаем приложение и завершаем выполнение при закрытии
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Запускаем программу, если файл выполняется как основной
    main()