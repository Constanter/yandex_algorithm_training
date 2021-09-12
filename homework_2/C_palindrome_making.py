def test(func):
    inputs = ['a', 'ab','cognitive']
    results = [0, 1, 4]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(string):
    max_len = int(len(string) / 2) if len(string) % 2 == 0 else int((len(string) - 1) / 2)
    counter = 0
    for i in range(max_len):
        if string[i] != string[-1-i]:
            counter += 1
    return counter

test(func)