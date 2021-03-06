# 4. Реализовать два небольших скрипта:
# - итератор, генерирующий целые числа, начиная с указанного;
# - итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении
# числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

from itertools import count, cycle

print('Первый скрипт')

while True:
    try:
        start_num = int(input('Введите стартовое число (целое): '))
        break
    except ValueError:
        print('Ошибка! Введены неверные данные.')

while True:
    iter_num_ = input('Введите число итераций (натуральное): ')
    if iter_num_.isdigit():
        iter_num = int(iter_num_)
        break
    else:
        print('Ошибка! Введены неверные данные.')


for el in count(start_num):
    if el >= start_num + iter_num:
        break
    else:
        print(el)

input('Нажмите Enter')
print('Второй скрипт')
iter_num = int(input('Введите число итераций (натуральное): '))

my_list = ['а', 'б', 'в', 'г', 'д']
c = 0
for el in cycle(my_list):
    if c >= iter_num:
        break
    print(el)
    c += 1
