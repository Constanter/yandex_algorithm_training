def test(func):
    inputs = [[2, 2, 1], [4, 2, 5, 5, 1000, 1]]
    results = [1, 13]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    list_numbers = lst[1:]

    list_numbers.sort()
    return (sum(list_numbers[:-1]))

test(func)