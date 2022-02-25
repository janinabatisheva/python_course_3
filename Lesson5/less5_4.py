# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

def translate(s):
    s_ = s.split(' ')
    s_[0] = my_dict[s_[0]]
    result = ' '.join(s_)
    return result


my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

my_f1 = open('inp5_4.txt', 'r', encoding='utf-8')
my_f2 = open('out5_4.txt', 'w', encoding='utf-8')

en_list = my_f1.readlines()
ru_list = [translate(el) for el in en_list]

my_f2.writelines(ru_list)

my_f2.close()
my_f1.close()
