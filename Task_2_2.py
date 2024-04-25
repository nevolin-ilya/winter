lst = [13, 2, 34, 467, 5, 2456, 74]

mins = lst[0]

for i in lst:
    if mins > i:
        mins = i
print(mins)