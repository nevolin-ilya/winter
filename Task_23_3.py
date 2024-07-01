

lst = [1, 33, 5, 2, 8, 3]
def func(lst):
    res = []
    p = str("".join(map(str, lst)))
    for i in p:
        res.append(i)
    res.sort(reverse=True)
    print(res)
    return "".join(res)
print(func(lst))
