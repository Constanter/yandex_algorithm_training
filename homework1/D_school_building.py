def test(func):
    inputs = [[4, 1, 2, 3, 4], [3, -1, 0, 1]]
    results = [3, 0]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    num, l = lst[0], lst[1:]
    num = num // 2
    return l[num]


test(func)
