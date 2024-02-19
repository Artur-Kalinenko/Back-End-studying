def deiltel():
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(int(num1 / num2))
    except ValueError:
        print('You must enter a number, not a string')

deiltel()