
f_in = open("Task_10_1", "r", encoding="utf-8")
lst1 = f_in.readlines(1)
lst2 = f_in.readlines(2)
f_in.close()
print(lst1)
print(lst2)

f_out = open("Task_10_11", "w", encoding="utf-8")
res1 = []
res2 = []
for i in lst1:
    res1 += i.split()
print(res1[::-1])
for i in lst2:
    res2 += i.split()
print(res2[::-1])
f_out.close()

