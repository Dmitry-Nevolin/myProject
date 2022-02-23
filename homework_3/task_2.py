# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def data(name, surname, year, place, email, phone_number):
    print(f"Здравствуйте! {name} {surname}, {year} год рождения, город {place}, {email}, {phone_number} ")


data(name=input("Имя: "), surname=input("Фамилия: "), year=input("Год рождения: "),
     place=input("Город: "), email=input("Email: "), phone_number=input("Номер телефона: "))
