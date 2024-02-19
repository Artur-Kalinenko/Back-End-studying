def valid_braces(string):
    new_list = []
    string = string.split()
    for char in string:
        if (char.index(char) % 2 == 0) and (char == '{' or char == '[' or char == '('):
            new_list.append(True)
        elif (char.index(char) % 2 == 1) and (char == '}' or char == ']' or char == ')'):
            new_list.append(True)
    return print(new_list)



valid_braces("())({}}{()][][")