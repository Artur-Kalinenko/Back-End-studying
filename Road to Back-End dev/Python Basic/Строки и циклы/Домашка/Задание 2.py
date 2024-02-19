some_string = 'ротатор'  # мим, дед, наган, заказ, кабак, казак, мадам, шалаш, ротатор
some_string = some_string.lower()
len_counter = len(some_string) // 2
substring_1 = some_string[0:len_counter]
substring_2 = some_string[-len_counter:]
substring_2_reversed = substring_2[::-1]
if substring_1 == substring_2_reversed:
    print('Полиндром')
else:
    print('Не полиндром')
