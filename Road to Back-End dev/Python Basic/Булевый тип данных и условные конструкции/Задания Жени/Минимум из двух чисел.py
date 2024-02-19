a, b = map(int, input('Enter 2 numbers: ').split())

# if a > b:
#     print(b)
# else:
#     print(a)

min_number = a if a < b else b
print(min_number)
