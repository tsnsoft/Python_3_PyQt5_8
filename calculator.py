# Файл calculator.py
# Содержит класс Calculator для выполнения вычислений по заданной формуле

import math  # Для математических вычислений (sin, cos, pow)
from PyQt5.QtWidgets import QTableWidgetItem  # Для работы с элементами таблицы


class Calculator:
    """
    Класс для выполнения вычислений по формуле
    """

    #    Y_i = \frac{\sqrt[3]{(\sum K_i)^2} * [\sin^2(K_i) - \cos^2(K_{i-1})]^3}{\prod K_{i-1}}
    #    для диапазона i = 1..10, где для i = 0 возвращается 'none'.

    def __init__(self):
        """Инициализирует объект калькулятора без параметров."""
        pass

    def calculate(self, table_widget):
        """
        Выполняет вычисления по формуле для каждой строки таблицы и заполняет второй столбец.
        :param table_widget: Виджет таблицы с данными в первом столбце
        :return: None, результаты записываются в таблицу
        """
        #        Формула: Y_i = \frac{\sqrt[3]{(\sum K_i)^2} * [\sin^2(K_i) - \cos^2(K_{i-1})]^3}{\prod K_{i-1}}, i = 1..10

        # Проверяем корректность данных в первом столбце перед вычислениями
        if self._validate_data(table_widget):
            i = 1  # Начинаем с i = 1, как указано в формуле (i = 1..10)
            j = 1  # Второй столбец для результатов
            multiplication_of_k_i_minus_1 = 1  # Инициализируем произведение элементов K(i-1)
            sum_of_k_i = 0  # Инициализируем сумму элементов K(i)

            # Инициализируем сумму для i = 0 (первая строка) перед началом цикла
            item_0 = table_widget.item(0, 0).text()
            sum_of_k_i += int(item_0)  # Добавляем значение первой строки

            # Проходим по строкам с i = 1 до 9 (10 строк, индексы 0-9)
            while i < table_widget.rowCount():
                # Получаем значение текущей строки из первого столбца
                item = table_widget.item(i, 0).text()
                sum_of_k_i += int(item)  # Обновляем сумму, включая текущий элемент

                try:
                    # Получаем значение предыдущей строки K(i-1)
                    item_minus_1 = table_widget.item(i - 1, 0).text()
                    # Умножаем произведение на значение предыдущей строки
                    multiplication_of_k_i_minus_1 *= int(item_minus_1)

                    # Вычисляем разность квадратов синуса текущего и косинуса предыдущего элемента
                    difference_of_sin_of_k_i_and_cos_of_k_minus_1 = (math.sin(int(item)) ** 2 -
                                                                     math.cos(int(item_minus_1)) ** 2)

                    # Вычисляем результат по формуле: (кубический корень * куб разности) / произведение
                    answer = ((((sum_of_k_i ** 2) ** (1 / 3.0)) *
                               difference_of_sin_of_k_i_and_cos_of_k_minus_1 ** 3) /
                              float(multiplication_of_k_i_minus_1))

                    # Записываем результат во второй столбец с точностью до 10 знаков
                    table_widget.setItem(i, j, QTableWidgetItem(str(format(answer, ".10f"))))
                except Exception:
                    # Если возникает ошибка (например, отсутствие K(i-1) для i=1), записываем 'none'
                    table_widget.setItem(i, j, QTableWidgetItem('none'))

                i += 1  # Переходим к следующей строке

            # Для первой строки (i=0) устанавливаем 'none', так как формула не применима
            table_widget.setItem(0, j, QTableWidgetItem('none'))
        else:
            # Выводим сообщение об ошибке, если данные некорректны (хотя это делается в основном коде)
            pass  # Логика вывода ошибки оставлена для основного кода

    def _validate_data(self, table_widget):
        """
        Проверяет, что все значения в первом столбце таблицы можно преобразовать в числа.
        :param table_widget: Виджет таблицы с данными
        :return: True, если данные корректны, False, если есть ошибки
        """
        i = 0  # Индекс текущей строки
        while i < table_widget.rowCount():
            try:
                # Пробуем преобразовать значение в float для проверки корректности
                float(table_widget.item(i, 0).text())
                i += 1  # Переходим к следующей строке, если преобразование успешно
            except Exception:
                # Возвращаем False, если преобразование невозможно (не число)
                return False
        # Возвращаем True, если все значения корректны
        return True
