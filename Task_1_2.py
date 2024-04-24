x = int(input())

y = int(input())

z1 = (x + y)
z2 = (x - y)
z3 = (x*y)
z4 = (x/y)
z5 = (x//y)

list1 = [z1, z2, z3, z4, z5]
Max1 = max(list1)
print("Наибольшее число", Max)

#второй вариант

x = int(input())

y = int(input())

z1 = (x + y)
z2 = (x - y)
z3 = (x*y)
z4 = (x/y)
z5 = (x//y)

if z1 > z2:
    max = z1
else:
    max = z2

if z3 > max:
    max = z3
else:
    max = max
if z4 > max:
    max = z4
else:
    max = max
if z5 > max:
    max = z5
else:
    max = max

print(max)