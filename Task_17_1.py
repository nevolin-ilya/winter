
import re


def replace_doubles(str):
    new_str = str.lower()
    pattern = r'(\w+)(\s+\1)+'
    return re.sub(pattern, r'\1', new_str)

print(replace_doubles(s))