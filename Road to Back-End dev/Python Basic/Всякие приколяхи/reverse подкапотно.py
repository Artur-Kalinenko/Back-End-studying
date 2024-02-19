my_list = [12, 43, 45, 657, 75, 676]

def reverser(lst):
    my_list2 = []
    sizer = len(my_list) - 1
    while sizer >= 0:
        my_list2.append(my_list[sizer])
        sizer -= 1
    return print(my_list2)

reverser(my_list)

