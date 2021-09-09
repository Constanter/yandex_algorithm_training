def test(func):
    inputs = [[-1, 0, 1], [42, 1, 6],
              [0, 0, 0], [44, 7, 4],
              [1, 4, 0]
              ]
    results = [3, 6, 0, 1, 3]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    end_code_task, interactor, checker = lst[0], lst[1], lst[2]
    if interactor == 6:
        return 0
    elif interactor == 7:
        return 1
    elif interactor == 4:
        if end_code_task != 0:
            return 3
        else:
            return 4
    elif interactor == 1:
        return checker
    elif interactor == 0:
        if end_code_task != 0:
            return 3
        else:
            return checker
    else:
        return interactor

test(func)
