def solution(s):
    some_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_list = []
    for char in s:
        if char in some_string:
            new_list.append(f' {char.lower()}')
        else:
            new_list.append(char)
    return ''.join(new_list)


print(solution("breakCamelCase"))
