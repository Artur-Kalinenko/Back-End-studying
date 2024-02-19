horizontal_square1 = int(input('Введите значение от 1 до 8: '))
vertical_square1 = int(input('Введите значение от 1 до 8: '))
horizontal_square2 = int(input('Введите значение от 1 до 8: '))
vertical_square2 = int(input('Введите значение от 1 до 8: '))

if (horizontal_square1 - horizontal_square2 == 1 or horizontal_square1 - horizontal_square2 == -1 or horizontal_square1 - horizontal_square2 == 0) and (vertical_square1 - vertical_square2 == 1 or vertical_square1 - vertical_square2 == -1 or vertical_square1 - vertical_square2 == 0):
    print('yes')
else:
    print("no")