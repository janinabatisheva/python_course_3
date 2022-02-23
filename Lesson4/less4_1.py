# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчёта заработной платы сотрудника. Используйте в
# нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv

try:
    script_name, hours, scale, bonus = argv
    pay = int(hours) * int(scale) + int(bonus)
    print("Зарплата: ", pay)
except ValueError:
    print("Ошибка! Введены неверные данные или недостаточно данных.")
