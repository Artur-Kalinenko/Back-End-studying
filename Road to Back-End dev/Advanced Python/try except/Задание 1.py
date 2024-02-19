some_list = [1, 2, 3, 4, 5]
try:
    print(some_list[6])
except IndexError:
    print('List index out of range')
