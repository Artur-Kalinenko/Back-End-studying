some_number = int(input('Вводи число, падла: '))
result = 0
while some_number >= 0:
    result += some_number
    print(result)
    some_number = int(input('Вводи число, падла: '))
    if some_number < 0:
        print(result)
