def get_middle1(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2 - 1] + s[len(s) // 2]


print(get_middle1('test'))
