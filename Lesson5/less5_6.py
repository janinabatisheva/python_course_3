# 6. Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно
# входить и количество занятий. Необязательно, чтобы для каждого
# предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.


def get_number(s):
    s_ = []
    for el in s:
        if str(el).isdigit():
            s_.append(el)
    if s_:
        return int(''.join(s_))
    else:
        return 0


def classes(s):
    s_ = s.split(':')
    if len(s_) > 1:
        result = sum([get_number(el) for el in s_[1].split()])
        return result
    else:
        return 0


def name(s):
    s_ = s.split(':')
    return s_[0]


with open('inp5_6.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()


classes_dict = {name(s): classes(s) for s in content if len(s) > 1}
print(classes_dict)
