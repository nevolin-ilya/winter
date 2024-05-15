s = input()
k1 = []
k2 = []

m = s.lower().split(".")

print(m)
print(list(m[0]))
for x in m[0]:
    if x.islower():
        k1.append(x)
for x in m[1]:

    if x.islower():
        k2.append(x)

k1.sort()
k2.sort()

print(k1 == k2)