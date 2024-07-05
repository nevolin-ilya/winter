import re
def text(s):
     s1 = s.lower()
     s2 = s1.title()
     s2.replace(" ", '')
     return s2

print(text("неВоЛин иЛья сЕРГееВИч"))


