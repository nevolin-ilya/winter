
from collections import Counter
def number(lst):
    count = Counter(lst)
    for k, v in count.items():
        if v == 1:
            return k

print(number([3,1,1,1,1,1]))