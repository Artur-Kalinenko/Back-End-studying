def capitalizer(some_string):
    some_string = some_string.split()
    # some_list = []
    # for i in some_string:
    #     some_list.append(i.capitalize())
    # return print(some_string)
    new_string = list(map(str.capitalize, some_string))
    new_string = ' '.join(new_string)
    return print(new_string)


capitalizer('сухарики мега пачка со вкусом краба семьдесят грамм')