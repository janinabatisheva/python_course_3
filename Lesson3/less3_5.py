# 5. Программа запрашивает у пользователя строку чисел,
# разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь
# введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ
# введён после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого
# завершить программу.


def input_nums():
    """Функция запрашивает данные у пользователя и формирует из них список."""
    num_string = input('Введите несколько чисел через пробел: ')
    num_list = num_string.split()
    return num_list


def is_float(el):
    """Функция проверяет соответствие данных типу float."""
    try:
        if abs(float(el)) >= 0:
            return True

    except ValueError:
        return False


def check_num(el):
    """Функция проверяет, является ли аргумент числом или спецсимволом"""
    if is_float(el):
        return True

    elif el.upper() == stop_symb:
        return False


stop_symb = 'Q'

print(f'Эта программа суммирует числа, стоп символ - {stop_symb}.')

result = 0

while True:
    li = input_nums()
    stop = False
    err = False

    for el in li:
        if check_num(el):
            result += float(el)
        elif check_num(el) == False:
            stop = True
            break
        else:
            err = True

    if err:
        print('Ошибка! Введены некорректные данные.')

    print(f'Сумма введенных чисел: {result}')

    if stop:
        break
