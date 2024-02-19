def number_of_words(some_string):
    some_string = some_string.strip()
    counter = 1
    for char in some_string:
        if char == ' ':
            counter += 1
    return print(counter)   # можно решить через сплит


number_of_words('Возможно ты не понимала меня, не принимала меня, но сейчас самое время это изменить')