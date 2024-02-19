
def some_func():
    some_str = input('Enter some string: ')
    file = open('Задание 2.txt', 'w')
    file.write(some_str)
    file.close()
    file = open('Задание 2.txt', 'r')
    print(file.read())
    file.close()


some_func()