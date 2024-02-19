def power(a, n):
    result = 1
    if n > 0:
        while n > 0:
            result *= a
            n -= 1
        return print(result)
    else:
        while n < 0:
            result *= a
            n += 1
    return print(1 / result)


power(2,     -15)