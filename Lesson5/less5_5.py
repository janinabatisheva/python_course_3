# Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделённых пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить её на экран.

from random import randint

li_1 = [str(randint(0, 20)) for _ in range(10)]

with open('out5_5.txt', 'w+', encoding='utf-8') as my_f:
    my_f.write(' '.join(li_1))

    my_f.seek(0)
    content = my_f.read()
    print(f'Содержимое файла: {content}')

    total = sum([int(el) for el in content.split(' ')])
    print(f'Сумма чисел: {total}')
