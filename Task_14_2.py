def sum(n):
    for i in range(n):
        if n < 10:
            print(n)
            return n
        else:
            x = n%10 + sum(n//10)
            print(n, x)
            return x
print(sum(int(input())))