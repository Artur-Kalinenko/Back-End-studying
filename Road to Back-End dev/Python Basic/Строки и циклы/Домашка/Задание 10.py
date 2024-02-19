some_string = ' 412sjnfjk,      , , , , ??????!!!!!!:::::::qjeriojwer , ,, kfj '
some_string = list(some_string)
new_str = []
for i in some_string:
    if i != ' ' and i != ',' and i != '.' and i != ':' and i != '?' and i != '!':
        new_str.append(i)
new_str = ''.join(new_str)
print(new_str)
