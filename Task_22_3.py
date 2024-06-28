
import keyword
lst = keyword.kwlist
dct = {key:'<kw>' for key in lst}
s = input().split()
res = [dct.get(item, item) for item in s]
print(" ".join(res))