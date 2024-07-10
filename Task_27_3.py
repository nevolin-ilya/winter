
def counter(lst):
    count = 0
    for i in lst:
        if (type(i) == type([])):
            count = count + counter(i) + 1
        else:
            count += 1
    return count

print(counter([1, 2, [3, 4, [5], [6, 7]]]))
