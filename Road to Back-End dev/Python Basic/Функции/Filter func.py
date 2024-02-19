some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def check_is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def greeting():
    return 'hello'

def my_filter(func, my_list):
    new_list = []
    for n in func:
        if my_list(n) == True:
            new_list.append(n)
    return print(list(set(new_list)))


my_filter(some_list, check_is_even)
print(list(map(check_is_even, some_list)))