dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 1:{0:1111, 1:2222, 2:3333}}, 1:11}, 2:11}
def f(dct, x):
    res = []
    for k, v in dct.items():
        if k == x:
            res.append(v)
        elif type(k) == str:
            pass
        elif type(v) == dict:
            res.extend(f(v, x))
    print(res)
    return res
print(f(dct, 1))