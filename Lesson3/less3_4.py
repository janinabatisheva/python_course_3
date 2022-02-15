# 4. Программа принимает действительное положительное
# число x и целое отрицательное число y. Выполните возведение
# числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без
# встроенной функции возведения числа в степень.


def my_func_1(base, power):
    """Функция реализованная с помощью оператора ** ."""
    result = base ** power
    return result


def my_func_2(base, power):
    """Функция реализованная с помощью цикла."""
    if power < 0:
        result = 1
        for n in range(-1, power - 1, -1):
            result = result / base
    else:
        result = None
    return result


while True:
    try:
        base = float(input('Введите положительное число - основание степени: '))
        power = int(input('Введите целое отрицательное число - показатель степени: '))
        if base > 0 and power < 0:
            break
        else:
            print('Ошибка: неверный знак числа.')
    except ValueError:
        print('Ошибка: введены нечисловые данные.')

print(my_func_1(base, power))
print(my_func_2(base, power))
