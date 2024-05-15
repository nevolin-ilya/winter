s = input().split()

print(s)

res = 0

if s[1] == "+":
    res = int(s[0]) + int(s[2])
if s[1] == "-":
    res = int(s[0]) - int(s[2])
if s[1] == "*":
    res = int(s[0]) * int(s[2])
if s[1] == "/":
    res = int(s[0]) / int(s[2])

print(int(res))