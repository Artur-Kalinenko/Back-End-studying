def big_boys(some_list):
    # new_list = []
    # for i in some_list:
    #     new_list.append(i.upper())
    # return print(new_list)
    new_list = list(map(str.upper, some_list))
    return print(new_list)

big_boys(['Artur', 'Misha', 'Zheka', 'krab'])