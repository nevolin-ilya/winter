
def fb(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m//(a + b)


x = int(input())
y = int(input())
print(fb(x, y))


