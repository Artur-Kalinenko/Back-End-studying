x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

if abs(x_1 - x_2) == abs(y_1 - y_2) or x_1 == x_2 or y_1 == y_2:
    print('yes')
else:
    print('no')
