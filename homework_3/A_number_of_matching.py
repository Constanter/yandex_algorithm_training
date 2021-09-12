def test(func):
    inputs = [[[1, 3, 2], [4, 3, 2]],
              [[1, 2, 6, 4, 5, 7], [10, 2, 3, 4, 8, ]],
              [[1, 7, 3, 8, 10, 2, 5], [6, 5, 2, 8, 4, 3, 7]],
              ]
    results = [2, 2, 5]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    return len(set.intersection(set(list_1), set(list_2)))

test(func)