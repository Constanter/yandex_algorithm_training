def test(func):
    inputs = [[1, 7, 9, 0], [1, 3, 3, 1, 0]]
    results = [1, 2]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    max_elem = lst[0]
    counter = 1
    for elem in lst[1:]:
        if elem != 0:
            if elem > max_elem:
                max_elem = elem
                counter = 1
            elif elem == max_elem:
                counter += 1
        else:
            break

    return counter

test(func)

""""
max_elem = int(input())
counter = 1
while True:
    a = int(input())
    if a != 0:
        if a > max_elem:
            max_elem = a
            counter = 1
        elif a == max_elem:
            counter += 1
    else:
        break


print(counter)
"""