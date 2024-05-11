summa = 0
n = 0
while True:
    i = int(input())
    if i == 0:
        break
    summa = summa + i
    n = n + 1
    sred = summa/n
print(sred)