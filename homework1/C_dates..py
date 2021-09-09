def test(func):
    inputs = [[1, 2, 2003], [2, 29, 2008]]
    results = [0, 1]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    x, y, z = lst[0], lst[1], lst[2]
    if (x < 13 and y > 12) or (x > 12 and y < 13) or (x == y):
        return 1
    else:
        return 0


test(func)
