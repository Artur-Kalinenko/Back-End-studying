file = open('Задание 1.txt', 'w')
file.write('Введем сюда новый')
file.close()

file = open('Задание 1.txt', 'r')
print(len(file.read().split()))
file.close()

