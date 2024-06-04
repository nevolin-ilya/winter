
def fun(x):
    lst = [int(i) for i in range(x)]
    for j in lst:
        if str(j) == str(j)[::-1]: yield j

g = fun(int(input()))
for i in g:
    print(i, end=" ")