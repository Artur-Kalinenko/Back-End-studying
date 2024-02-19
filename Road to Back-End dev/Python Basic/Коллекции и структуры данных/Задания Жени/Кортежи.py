some_tuple = ('Artur', 22, 'Programmer', ['Pachka', 'chipsov', 's', 'krabom', '70 gram'], 'Artur')
some_tuple_2 = ('DOLBOEB', 'ZHMIH')
mega_tuple = some_tuple + some_tuple_2
print(mega_tuple)
x, y = some_tuple_2
print(x, y)
print(mega_tuple.count('Artur'))
print(mega_tuple.index(22))
