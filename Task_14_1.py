
def sum(n):
    if n < 10:
        print(n)
        return 1
    else:
        x = 1 + sum(n//10)
        print(n, x)
        return x
print(sum(int(input())))

