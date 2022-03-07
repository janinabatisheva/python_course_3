# 2. Создайте собственный класс-исключение, обрабатывающий
# ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class ZeroDivErr(Exception):
    def __init__(self, divider):
        self.divider = divider

    def __str__(self):
        return "Ошибка: на ноль делить нельзя!"


class Num:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        if other.value != 0:
            return Num(self.value / other.value)
        else:
            raise ZeroDivErr(other.value)


try:
    value1 = float(input('Введите делимое: '))
    value2 = float(input('Введите делитель: '))
    num = Num(value1) / Num(value2)
    print(f'Частное равно: {num.value}')

except ZeroDivErr as err:
    print(err)
except ValueError:
    print('Ошибка! Введены некорректные данные.')
