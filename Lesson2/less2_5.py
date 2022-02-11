# 5. Реализовать структуру «Рейтинг», представляющую собой
# набор натуральных чисел, который не возрастает. У пользователя
# нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_list = [7, 5, 5, 3, 3, 2]

my_num = int(input('Please, insert your number (natural only): '))

flag = False

for i in range(len(my_list)):
    if my_num > my_list[i]:
        my_list.insert(i, my_num)
        flag = True
        break

my_list.append(my_num) if not flag else my_list.append(None)

print(my_list)
