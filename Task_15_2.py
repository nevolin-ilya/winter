
import re

def nambers(x):

    pattern = r"\w\d\d\d\w\w78|\w\d\d\d\w\w178"
    match1 = re.findall(pattern, x)
    return match1

print(nambers(input()))
