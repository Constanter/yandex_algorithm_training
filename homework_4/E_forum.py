counter = int(input())
num = 0
d = {}
while counter > num:
    num += 1
    inp = input()
    if inp == '0':
        for i in range(2):
            if i == 0:
                theme = input()
                d[num] = theme
            else:
                input()
    else:
        d[num] = int(inp)
        input()


def find(key):
    if type(key) == str:
        return key
    else:
        return find(d[key])


sum_dic = {}

for value in d.values():
    if type(value) == str and value not in sum_dic.keys():
        sum_dic[value] = 1
    else:
        val = find(value)
        sum_dic[val] += 1

sum_dic_list = sorted([(value, key) for key, value in sum_dic.items()], reverse=True)
max_el = sum_dic_list[0][0]

max_list = []

for key, value in sum_dic.items():
    if value == max_el:
        max_list.append(key)

result = []

for key, value in d.items():
    if value in max_list:
        result.append(key)
print(d[min(result)])