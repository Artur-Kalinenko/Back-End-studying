def parnie(some_list):
    new_list = []
    for i in some_list:
        if some_list.count(i) == 2:
            new_list.append(i)
    return print(new_list)


parnie([1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5])


