# 7. Спортсмен занимается ежедневными пробежками. В первый день
# его результат составил a километров. Каждый день спортсмен
# увеличивал результат на 10% относительно предыдущего. Требуется
# определить номер дня, на который результат спортсмена составит
# не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.

a = float(input('Введите a > 0: '))
b = float(input('Введите b > a: '))

days = 1

while a < b:
    a = float(f'{a * 1.1:.2f}')
    days += 1

print(f'На {days} день спортсмен достиг результата - не менее {b} километров.')
