horizontal_square1 = int(input('Введите значение от 1 до 8: '))
vertical_square1 = int(input('Введите значение от 1 до 8: '))
horizontal_square2 = int(input('Введите значение от 1 до 8: '))
vertical_square2 = int(input('Введите значение от 1 до 8: '))

if horizontal_square1 == horizontal_square2 or vertical_square1 == vertical_square2:
    print('YES')
else:
    print('NO')
