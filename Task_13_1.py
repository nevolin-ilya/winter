def fun(x):
    for i in range(x):
        if i % 2 != 1:
            yield -i
        else:
            yield i

g = fun(int(input()))
for i in g:
    print(i, end=" ")