dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11}, 2:11}
def f(dct):
    res = []
    for k, v in dct.items():
        print(k)
        if k == 1:
            res.append(v)
        elif type(k) == str:
            pass
        elif type(v) == dict:
            res.extend(f(v))
    print(res)
    return res
print(f(dct))