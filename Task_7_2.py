def max_sort(x):
    lst = []
    for i in x:
        for j in i:
            lst.append(j)
            lst.sort()
    return lst[-3:]

x = [[7,2,5], [6,3,9]]
print(max_sort(x))