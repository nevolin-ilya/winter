def f(s1, s2):
    count = 0
    for i, j in zip(list(s1), list(s2)):
        print(i, j)
        if i != j:
            count += 1
        else:
            count
    return count

print(f("ebd", "acd"))