some_string = 'аашкойруцщмукрщумц'
counter = 0
# for char in some_string:
#     if char == 'а' or char == 'я' or char == 'у' or char == 'ю' or char == 'о' or char == 'е' or char == 'ё' or char == 'э' or char == 'и' or char == 'ы':
#         counter += 1
vowels = 'аяуюоеёэиыАЯУЮЩЕЁЭИЫ'
for char in some_string:
    if char in vowels:
        counter += 1
print(counter)
