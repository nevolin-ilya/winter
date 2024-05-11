n = input()
s = n.split()
max = 0
for i in s:
    k = int(len(i))
    if max < k:
        max = k
print(max)
