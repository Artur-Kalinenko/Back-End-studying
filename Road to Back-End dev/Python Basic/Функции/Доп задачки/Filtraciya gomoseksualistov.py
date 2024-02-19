dev_list = ['Python', 'js', 'javaScriptik', 'Python', 'javaScriptulechka :*']


def is_gay(elem):
    return elem != 'Python'


gay_check = list(filter(is_gay, dev_list))
print(gay_check)
