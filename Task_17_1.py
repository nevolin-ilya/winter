

import re
s = "Программа прогрмма, которая удаляет удаляет повторяющеся слова слова в предложении"

res = s.lower()
numbers = res.split()
numbers_unique = list(dict.fromkeys(numbers))
print(numbers_unique)

