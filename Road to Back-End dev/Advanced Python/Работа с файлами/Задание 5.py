file = open('Задание 5.txt', 'w')
file.write('Строка1\nСтрока2\nСтрока3 будет тут')
file.close()

file = open('Задание 5.txt', 'r')
lines_list = []
while True:
    line = file.readline()
    if not line:
        break
    lines_list.append(line)
file.close()


def str_remover(some_list):
    try:
        some_list.pop(2)
        print(''.join(some_list))
    except IndexError:
        print('There is no such string')
        print(''.join(some_list))


str_remover(lines_list)
