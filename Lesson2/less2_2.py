# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
# и т. д. При нечётном количестве элементов последний сохранить
# на своём месте. Для заполнения списка элементов нужно
# использовать функцию input().

maxnum = int(input('Please, insert quantity of items: '))

li1 = []
for num in range(maxnum):
    item = input(f'Please, insert item number {num + 1}: ')
    li1.append(item)

print(li1)

for num in range(0, (maxnum + 1) // 2):
    if 2 * num + 1 in range(maxnum):
        li1[2 * num], li1[2 * num + 1] = li1[2 * num + 1], li1[2 * num]

print(li1)
