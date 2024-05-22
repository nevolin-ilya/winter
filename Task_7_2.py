def max_sort(x):
    lst = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            lst.append(j)

x = [[7,2,5], [6,3,9]]
print(max_sort(x))