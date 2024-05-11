n = input()
res = [int(x) for a,x in enumerate(str(n))]

print(res)
for i in res:
    print(i, "-", res.count(i))