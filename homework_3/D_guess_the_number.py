def test(func):
    inputs = [['10', '1 2 3 4 5', 'YES', '2 4 6 8 10', 'NO'],
              ['10', '1 2 3 4 5 6 7 8 9 10', 'YES', '1', 'NO', '2', 'NO',
               '3', 'NO', '4', 'NO', '6', 'NO', '7', 'NO', '8', 'NO', '9', 'NO', '10', 'NO']
              ]

    results = [[1, 3, 5], [5]]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    guess_version = set([i for i in range(1, int(lst[0]) + 1)])

    for ans in range(len(lst)):
        if lst[ans] == 'NO':
            buf = set(map(int, lst[ans - 1].split()))
            set.difference_update(guess_version, buf)
            buf = set()
        elif lst[ans] == 'YES':
            buf = set(map(int, lst[ans - 1].split()))
            set.intersection_update(guess_version, buf)
            buf = set()
    return list(guess_version)


test(func)