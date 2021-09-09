def test(func):
    inputs = [[5, 1, 1, ], [3, -1, -1],
              [4, 4, 4, ], [4, 2, 2],
              ]
    results = [0, 1, 2, 0]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    d, x, y = lst[0], lst[1], lst[2]

    def compute_distance(name):
        if name == 'A':
            return ((0 - x) ** 2 + (0 - y) ** 2) ** 0.5
        elif name == 'B':
            return ((d - x) ** 2 + (0 - y) ** 2) ** 0.5
        elif name == 'C':
            return ((0 - x) ** 2 + (d - y) ** 2) ** 0.5

    xa, xb, xc, ya, yb, yc = 0, d, 0, 0, 0, d
    a = (xa - x) * (yb - ya) - (xb - xa) * (ya - y)
    b = (xb - x) * (yc - yb) - (xc - xb) * (yb - y)
    c = (xc - x) * (ya - yc) - (xa - xc) * (yc - y)

    if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
        return 0
    else:
        result = []
        for i in ('A', 'B', 'C'):
            result.append(compute_distance(i))
        return result.index(min(result)) + 1


test(func)
