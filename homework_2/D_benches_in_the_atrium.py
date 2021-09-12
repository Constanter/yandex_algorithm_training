def test(func):
    inputs = [[5, 2, 0, 2], [13, 4, 1, 4, 8, 11], [14, 6, 1 ,6, 8, 11, 12, 13]]
    results = [[2], [4,8], [6, 8]]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    bench_length, cubes_num = lst[:2]
    list_of_legs = lst[2:]

    center = bench_length // 2

    if (bench_length%2 == 1) and (center in list_of_legs):
        return [center]
    else:
        for i, el in enumerate(list_of_legs):
            if el >= center:
                return [list_of_legs[i-1],list_of_legs[i]]
                break

test(func)