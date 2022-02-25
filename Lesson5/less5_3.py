# 3. Создать текстовый файл (не программно). Построчно записать
# фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести
# фамилии этих сотрудников. Выполнить подсчёт средней величины
# дохода сотрудников.

from functools import reduce


my_f = open('inp5_3.txt', 'r', encoding='utf=8')

data = []
for line in my_f:
    data.append(line.split())

has_low_salary = [el[0] for el in data if float(el[1]) < 20000]
print('Имеют зарплату менее 20 тысяч:')
print(*has_low_salary)

salary = [float(el[1]) for el in data]
sum_salary = reduce(lambda x, y: x + y, salary)
average_salary = round(sum_salary / len(salary), 2)
print(f'\nСредняя зарплата: {average_salary}')

my_f.close()
