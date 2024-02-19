def number_of_vowels(some_str):
    vowels = 'aeiouyAEIOUY'
    counter = 0
    for char in some_str:
        if char in vowels:
            counter += 1
    return print(counter)


number_of_vowels('Akveduk')