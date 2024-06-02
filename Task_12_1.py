def lst_index(lst):
    lst1 = []
    return [x for x, v in enumerate(lst) if v == min(lst)], [x for x, v in enumerate(lst) if v == max(lst)]

lst = [2, 1, 2, 4, 1, 7, 1, 1, 1]
print(lst_index(lst))



