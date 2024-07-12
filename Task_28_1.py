

def inv(spisok):
    count = 0
    for i, elm1 in enumerate(spisok):
        for elm2 in spisok[i + 1:]:
            if elm1 > elm2:
                count += 1
    return count
print(inv([1,5,4,3,2,1]))