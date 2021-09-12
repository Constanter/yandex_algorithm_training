def test(func):
    inputs = [[1, 2, 2, 3, 3, 3], [4, 3, 5, 2, 5, 1, 3, 5]]
    results = [[1], [4, 2, 1]]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    return [i for i in lst if lst.count(i) == 1]


test(func)