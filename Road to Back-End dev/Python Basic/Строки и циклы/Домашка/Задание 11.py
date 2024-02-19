some_list = [3, 2, 4, 2, 5, 9, 2, 6, 5, 3, 5]
min_element = some_list[0]

for element in some_list:
    if element < min_element:
        min_element = element

while min_element in some_list:
    some_list.remove(min_element)

min_element = some_list[0]

for element in some_list:
    if element < min_element:
        min_element = element
print(min_element)
