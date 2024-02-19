class1, class2, class3 = map(int, input().split())

amount_of_tables_for_class1 = class1 // 2 + class1 % 2
amount_of_tables_for_class2 = class2 // 2 + class2 % 2
amount_of_tables_for_class3 = class3 // 2 + class3 % 2

total_amount_of_tables = amount_of_tables_for_class1 + amount_of_tables_for_class2 + amount_of_tables_for_class3

print(total_amount_of_tables)
