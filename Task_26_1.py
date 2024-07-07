def stroka(str1, str2):
    lst1 = list(str1)
    lst2 = list(str2)
    print(lst1)
    print(lst2)
    count = 0
    for i, j in zip(lst1, lst2):
        if ord(i) != ord(j):
            count += 1
            print(count)
    if count == 2:
        return False
    elif abs(len(lst1) - len(lst2)) > 1:
        return False
    elif abs(len(lst1) - len(lst2)) == 1 & count == 1:
        return False
    elif (str1 == ' ') & (str2 == '') or (str2 == ' ') & (str1 == ''):
        return False
    else:
        return True

print(stroka("abc", "acb"))
