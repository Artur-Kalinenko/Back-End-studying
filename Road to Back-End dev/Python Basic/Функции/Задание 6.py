def factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return print(factorial)


factorial(11)