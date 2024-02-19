from datetime import datetime

name = input("Please, enter your name: ")
born_year = int(input("Please, enter an age when you were born: "))
current_time = datetime.now()  # В этой переменной у нас хранится текущее время
current_year = current_time.year  # Тут мы выводим из текущего времени только актуальный год
user_age = current_year - born_year

print(f"Your name is: {name}, your age is: {user_age}")
