# 1. Создать программный файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем. Об окончании
# ввода данных будет свидетельствовать пустая строка.

my_f = open("out5_1.txt", "a", encoding='utf-8')

while True:
    my_str = input('Введите строку данных: ')
    if len(my_str) > 0:
        my_f.write(my_str + '\n')
    else:
        break

my_f.close()