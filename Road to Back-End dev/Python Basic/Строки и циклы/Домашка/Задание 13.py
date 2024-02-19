lucky_number = 3
number = int(input('Введите число от 1 до 10: '))
while number != lucky_number:
    if number == 0:
        print('better luck next time!')
        break
    else:
        print('Попробуйте еще раз: ')
        number = int(input('Введите число от 1 до 10: '))
else:
    print('you won')


