def spiralize(number):
    x = 1
    y = 2
    z = 0
    n = 0

    while x <= pow(number, 2):
        z += x
        x += y
        n += 1
        if n == 4:
            y += 2
            n = 0
    return z


print(spiralize(501))
