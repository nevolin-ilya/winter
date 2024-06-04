st = input()
lst = [int(i) for i in st]
def valera(lst):
    for i in lst:
        if i%2 != 0: yield i

gf = valera(lst)
for i in gf:
    print(i, end=" ")