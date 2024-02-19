# Функция trunc выполняет отсечение дробной части и оставляет только целую часть числа
#
# Функция floor выполняет округление вниз до ближайшего целого числа
#
# Функция ceil выполняет округление вверх до ближайшего целого числа

import math
# n = int(input())
# print(math.ceil(n / 10))

# n = int(input())
# print(math.ceil(n / 4))

# a, b, c = map(int, input().split())
# print(math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2))

l, w, h = map(int, input().split())
p = (l + w) * 2
s = p * h
result = math.ceil(s / 16)
print(result)