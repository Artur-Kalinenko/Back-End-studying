a = int(input())
b = int(input())
l = int(input())
n = int(input())

length_of_a = (n - 1) * a * 2 + a
length_of_b = (n - 1) * b * 2

full_length = length_of_a + length_of_b + l * 2

print(full_length)
