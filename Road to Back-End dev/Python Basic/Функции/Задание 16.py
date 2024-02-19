def dict_of_vowels(*args):
    mega_word = args
    mega_word = mega_word.lower()
    some_dict = {}
    counter_of_a = 0
    counter_of_e = 0
    counter_of_i = 0
    counter_of_o = 0
    counter_of_u = 0
    counter_of_y = 0
    for char in mega_word:
        if char == 'a':
            counter_of_a += 1
            some_dict.update({'a': counter_of_a})
        elif char == 'e':
            counter_of_e += 1
            some_dict.update({'e': counter_of_e})
        elif char == 'i':
            counter_of_i += 1
            some_dict.update({'i': counter_of_i})
        elif char == 'o':
            counter_of_o += 1
            some_dict.update({'o': counter_of_o})
        elif char == 'u':
            counter_of_u += 1
            some_dict.update({'u': counter_of_u})
        elif char == 'y':
            counter_of_y += 1
            some_dict.update({'y': counter_of_y})
    return print(some_dict)


dict_of_vowels('Aachkaouo', 'AKrab')
