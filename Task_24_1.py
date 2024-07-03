def sort(lst):
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
s = [3, 5, 2, 66, 1, 6]
print(sort(s))

