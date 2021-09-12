def test(func):
    inputs = [[2, 0, 1, 1, 0, 1, 0, 2, 1, 2,]]
    results = [3]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    house_index = [i for i,el in enumerate(lst) if el == 1]
    shop_index = [i for i,el in enumerate(lst) if el == 2]

    def computer(num, lst):
        result = []
        for el in lst:
            if el > num:
                result.append(el-num)
            else:
                result.append(num-el)
        return min(result)

    list_distances = []
    for i in house_index:
        list_distances.append(computer(i, shop_index))

    return max(list_distances)

test(func)