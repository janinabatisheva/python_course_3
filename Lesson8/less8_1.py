# 1. Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:
    def __init__(self, date_str):
        self.date =[int(el) for el in date_str.split('-')]


    @classmethod
    def get_date(cls):
        date_str = input('Введите дату в формате дд-мм-гггг: ')
        if Date.validate_date(date_str):
            d = cls(date_str)
            return d.date
        else:
            return ''

    @staticmethod
    def validate_date(date_str):
        date_list = date_str.split('-')
        days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if len(date_list) == 3 and date_list[0].isdigit() and date_list[1].isdigit() and date_list[2].isdigit():
            if int(date_list[1]) > 0 and int(date_list[1]) < 13 and int(date_list[0]) > 0 and int(date_list[0]) < days_in_month[int(date_list[1])]:
                return True
            else:
                print('Ошибка! Число или месяц выходят за границы требуемого диапазона.')
                return False
        else:
            print('Ошибка! Дата введена некорректно.')
            return False


num_date = Date.get_date()
print(*num_date)

