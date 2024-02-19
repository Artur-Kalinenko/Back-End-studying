horizontal_square1 = int(input('Введите значение от 1 до 8: '))
vertical_square1 = int(input('Введите значение от 1 до 8: '))
horizontal_square2 = int(input('Введите значение от 1 до 8: '))
vertical_square2 = int(input('Введите значение от 1 до 8: '))
color_of_square1 = None
color_of_square2 = None

if horizontal_square1 % 2 == 1 and vertical_square1 % 2 == 0:
    if horizontal_square1 % 2 == 0 and vertical_square1 % 2 == 1:
        color_of_square1 = "red"
        print(color_of_square1)
    else:
        color_of_square1 = "white"
        print(color_of_square1)
else:
    if horizontal_square1 % 2 == 0 and vertical_square1 % 2 == 1:
        color_of_square1 = "white"
        print(color_of_square1)
    else:
        color_of_square1 = "red"
        print(color_of_square1)

if horizontal_square2 % 2 == 1 and vertical_square2 % 2 == 0:
    if horizontal_square2 % 2 == 0 and vertical_square2 % 2 == 1:
        color_of_square2 = "red"
        print(color_of_square2)
    else:
        color_of_square2 = "white"
        print(color_of_square2)
else:
    if horizontal_square2 % 2 == 0 and vertical_square2 % 2 == 1:
        color_of_square2 = "white"
        print(color_of_square2)
    else:
        color_of_square2 = "red"
        print(color_of_square2)

if color_of_square1 == color_of_square2:
    print("YES")
else:
    print("NO")




