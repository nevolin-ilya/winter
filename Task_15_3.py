
import re

def nambers(x):
    #s = x.split(" ")
    pattern = r"\+7(812)\d\d\d-\d\d\d\d|\+7(812)\d\d\d-\d\d-\d\d|\+7(921)\d\d\d-\d\d\d\d|\+7(921)\d\d\d-\d\d-\d\d"
    match1 = re.findall(pattern, x)
    return match1

print(nambers(input()))