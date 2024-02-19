file = open('Задание 3.txt', 'w')
file.write('Some string2')
# file.close()

file = open('Задание 3.txt', 'r')
content = file.read()
file.close()

file1 = open('Задание 3 copy.txt', 'a')
file1.write(content)
file1.close()

# with open('Задание 3.txt', 'w') as file:
#     file.write('Some string')
#
# # Чтение из файла 'Задание 3.txt'
# with open('Задание 3.txt', 'r') as file:
#     content = file.read()
#     print(content)
#
# # Запись содержимого файла 'Задание 3.txt' в файл 'Задание 3 copy.txt'
# with open('Задание 3 copy.txt', 'w') as file1:
#     file1.write(content)