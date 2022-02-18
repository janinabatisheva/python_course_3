# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Осуществить вывод данных
# о пользователе одной строкой.


def personal_info(name, surname, birth_year, city, mail, phone):
    print(f'{name} {surname}, год рождения {birth_year}, город {city}, телефон {phone}, e-mail: {mail}')


user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_birth_year = input('Введите год рождения: ')
user_city = input('Введите город: ')
user_phone = input('Введите телефон: ')
user_mail = input('Введите e-mail: ')

personal_info(name=user_name,
              surname=user_surname,
              birth_year=user_birth_year,
              city=user_city,
              mail=user_mail,
              phone=user_phone)
