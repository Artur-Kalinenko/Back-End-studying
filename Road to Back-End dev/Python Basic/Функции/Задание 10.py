def anagrams(str_1, str_2):
    sorted_string_1 = ''.join(sorted(str_1))
    sorted_string_2 = ''.join(sorted(str_2))
    if sorted_string_1 == sorted_string_2:
        return print(True)
    else:
        return print(False)


anagrams('австралопитек', 'ватерполистка')
anagrams('обезьянство', 'светобоязнь')
anagrams('обезьянствомо', 'светобоязнь')
