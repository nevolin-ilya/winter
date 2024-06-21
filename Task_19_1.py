import itertools

n = int(input())
s = [10, 50, 100, 200, 500, 1000, 2000, 5000]

for i in range(len(s)):
    comb = list(itertools.combinations(s, n))
print(comb)

for i in comb:
    k = list(i)
    print(sum(k), end=" ")