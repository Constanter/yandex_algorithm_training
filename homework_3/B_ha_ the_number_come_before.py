def test(func):
    inputs = [[1, 2, 3, 2, 3, 4]]
    results = [['NO', 'NO', 'NO', 'YES', 'YES', 'NO']]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    d = {}
    res = []
    for i in lst:
        if i in d:
            res.append('YES')
        else:
            res.append('NO')
            d[i] = 1
    return res


test(func)