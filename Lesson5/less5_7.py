# 7. Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами
# и их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json


def get_number(s):
    s_ = []
    for el in s:
        if str(el).isdigit():
            s_.append(el)
    if s_:
        return int(''.join(s_))
    else:
        return 0


def get_name(s):
    s_ = s.split()
    return s_[0]


def get_result(s):
    s_ = s.split()
    return get_number(s_[2]) - get_number(s_[3])


with open('inp5_7.txt', 'r', encoding='utf-8') as f1:
    content = f1.readlines()

nett = {get_name(s): get_result(s) for s in content}
profits = [nett[firm] for firm in nett if nett[firm] > 0]

result = [nett, {"average_profit": round(sum(profits) / len(profits))}]

with open('out5_7.json', 'w', encoding='utf-8') as f2:
    json.dump(result, f2, ensure_ascii=False)

# with open('out5_7.json', 'r', encoding='utf-8') as f3:
#    data = json.load(f3)
#    print(data)
