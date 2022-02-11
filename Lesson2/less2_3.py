# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.

# Первое решение через list:
seasons = [
    'winter', 'winter', 'spring', 'spring', 'spring', 'summer',
    'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter'
]

monthnum = int(input('Please, insert the month (number): ')) - 1
print(f'The season is {seasons[monthnum]}.')

# Второе решение через dict:
seasons = {
    1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
    7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'
}

monthnum = int(input('Please, insert the month (number): '))
print(f'The season is {seasons.get(monthnum)}.')

# Третье решение через совмещение list и dict:

seasons = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}

monthnum = int(input('Please, insert the month (number): '))

for season in seasons.keys():
    if monthnum in seasons.setdefault(season):
        print(f'The season is {season}.')
