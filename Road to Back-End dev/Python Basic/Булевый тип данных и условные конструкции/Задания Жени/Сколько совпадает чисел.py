a, b, c = map(int, input("Enter 3 numbers: ").split())

if a == b and a != c:
    print(2)
elif a == b and a == c:
    print(3)
else:
    print(0)
