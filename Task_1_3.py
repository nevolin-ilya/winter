x = int(input())

y = int(input())

z1 = (x + y)
z2 = (x - y)
z3 = (x*y)
z4 = (x/y)
z5 = (x//y)

list1 = [z1, z2, z3, z4, z5]
list1.sort()
print("Наибольшее число", list1[-2])