def zamena(lst):
    for i in range(len(lst) - 1):
        if (lst[i] == 'А' and lst[i + 1] == 'Г') or (lst[i] == 'Г' and lst[i + 1] == 'А'):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return ''.join(lst)

def dobavl(lst):
    res = []
    for i in range(len(lst) - 1):
        if (lst[i] == 'Ц' and lst[i + 1] == 'Т') or (lst[i] == 'Т' and lst[i + 1] == 'Ц'):
            res.append(lst[i])
            res.append("АГ")
        else:
            res.append(lst[i])
    res.append(lst[-1])
    return ''.join(res)

lst = list(input())
print(zamena(lst))