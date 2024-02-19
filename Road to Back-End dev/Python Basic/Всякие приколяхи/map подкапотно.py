my_list = [67, 234, 734, 14, 57, 234]


def delitel(num):
    return int(num / 2)


new_list = list(map(delitel, my_list))

print(new_list)


def my_map(func, iterable):
    list_govnoedov = []
    for i in iterable:
        result = func(i)
        list_govnoedov.append(result)
    return print(list_govnoedov)


new_list = my_map(delitel, my_list)
