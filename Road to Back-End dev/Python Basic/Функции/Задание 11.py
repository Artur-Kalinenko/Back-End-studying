
def dict_work(some_dict1, some_dict2):
    giga_dict = {**some_dict1, **some_dict2}
    return print(giga_dict)


dict_work({'number1': 1, 'number3': 1}, {'number': 2, 'number3': 5})