
import re

def nambers(x):

    pattern = r"\w\d\d\d\w\w78" or r"\w\d\d\d\w\w178"
    match = re.match(pattern, x)
    return bool(match)

print(nambers(input()))