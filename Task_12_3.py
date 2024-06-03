x = "1-3,5-8"
lst = x.split(",")
s = []
for k in lst:
    a, b = map(int, k.split("-"))
    for i in range(a, b + 1):
        s.append(i)

#print(a, b, end=" ")
print(s)