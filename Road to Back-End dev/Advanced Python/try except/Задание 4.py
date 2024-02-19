number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))
try:
    print(number_1 / number_2)
except ZeroDivisionError:
    print("You can't divide by 0")