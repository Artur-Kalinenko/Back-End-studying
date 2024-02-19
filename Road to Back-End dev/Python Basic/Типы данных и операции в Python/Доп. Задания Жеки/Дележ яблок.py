n = int(input("Enter the number of kids: "))
k = int(input("Enter the number of apples: "))

amount_of_apples_of_1_kid = k // n
basket = k % n

print(f"Каждый ребенок получит {amount_of_apples_of_1_kid} яблок.\n"
      f"В корзинке останется {basket} яблок.")
