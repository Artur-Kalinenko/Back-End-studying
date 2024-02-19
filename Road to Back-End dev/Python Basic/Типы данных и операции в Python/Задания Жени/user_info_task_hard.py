from datetime import datetime

name = input("Please, enter your name: ")
born_year = int(input("Please, enter a year when you were born: "))
born_month = int(input("Please, enter a month when you were born: "))
born_day = int(input("Please, enter a day when you were born: "))
born_date = (born_year, born_month, born_day)  # Создаем кортеж с датой рождения пользователя
current_time = datetime.now()  # В этой переменной у нас хранится текущее время
current_year = current_time.year  # Тут мы выводим из текущего времени только актуальный год
current_month = current_time.month
current_day = current_time.day
current_date = (current_year, current_month, current_day)  # Создаем кортеж текущей даты
user_age = current_date[0] - born_date[0], current_date[1] - born_date[1], current_date[2] - born_date[2]  # Вычисляем дату рождения пользователя
if user_age[1] or user_age[2] < 0:
    modified_user_age = (user_age[0] - 1,) + user_age[1:]  # Изменяем первый элемент кортежа с помощью среза
    print(f"Your name is: {name}, your age is: {modified_user_age[0]}")
else:
    print(f"Your name is: {name}, your age is: {user_age[0]}")
