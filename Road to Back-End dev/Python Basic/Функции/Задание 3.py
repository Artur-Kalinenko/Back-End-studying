def maximum_number(some_list):
    max_number = some_list[0]
    for i in some_list:
        if i > max_number:
            max_number = i
    return print(max_number)


maximum_number([800, 900, -1, 687])
