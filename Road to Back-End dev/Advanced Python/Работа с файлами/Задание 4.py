file = open('Задание 4(1 файл).txt', 'w')
file.write('Тут есть текст.\nИ тут есть текст.\nПачка чипсов')
file.close()

file1 = open('Задание 4(2 файл).txt', 'w')
file1.write('Тут есть текст.\nТут есть текста.')
file1.close()

file = open('Задание 4(1 файл).txt', 'r')
file1 = open('Задание 4(2 файл).txt', 'r')
lines_list_for_first_file = []
lines_list_for_second_file = []
while True:
    line = file.readline()
    if not line:
        break
    lines_list_for_first_file.append(line)
while True:
    line = file1.readline()
    if not line:
        break
    lines_list_for_second_file.append(line)
for i in lines_list_for_first_file:
    if i not in lines_list_for_second_file:
        print(i)
file.close()



