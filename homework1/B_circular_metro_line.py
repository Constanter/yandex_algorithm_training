def test(func):
    inputs = [[100, 5, 6], [10, 1, 9]]
    results = [0, 1]
    for i, (s, r) in enumerate(zip(inputs, results)):
        if func(s) == r:
            print(f'Test_{i}----passed')
        else:
            print(f'Test_{i}----failed')


def func(lst):
    number_of_station, in_station, out_station = lst[0], lst[1], lst[2]
    if out_station > in_station:
        direct_route = out_station - in_station - 1
        round_route = number_of_station - out_station + in_station - 1
        if direct_route < round_route:
            return direct_route
        else:
            return round_route
    else:
        direct_route = in_station - out_station - 1
        round_route = number_of_station - in_station + out_station - 1
        if direct_route < round_route:
            return direct_route
        else:
            return round_route


test(func)
