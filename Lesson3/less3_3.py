# 3. Реализовать функцию my_func(), которая принимает три
# позиционных аргумента и возвращает сумму наибольших двух аргументов.


def my_func(arg1=0, arg2=0, arg3=0):
    """Возвращает сумму двух наибольших чисел из трех данных"""
    my_tuple = (arg1, arg2, arg3)
    return sum(my_tuple) - min(my_tuple)


def convert_to_float(string):
    """Приводит аргумент к формату float, а если это невозможно, возвращает нулевое значение"""
    err = False
    try:
        result = float(string)
    except ValueError:
        err = True
        result = 0
    return (result, err)


while True:
    print('Пожалуйста, введите три числовых аргумента.')

    argument1 = convert_to_float(input('Первый аргумент: '))
    argument2 = convert_to_float(input('Второй аргумент: '))
    argument3 = convert_to_float(input('Третий аргумент: '))

    if argument1[1] or argument2[1] or argument3[1]:
        print('Ошибка! Введены неверные данные.')
    else:
        result = my_func(argument1[0], argument2[0], argument3[0])
        print(f'Сумма двух наибольших: {result}')
        break
