list_strings = []
while True:
    try:
        string = input().split()
        list_strings.append(string)
    except EOFError:
        break
summ = 0
for s in list_strings:
    summ += int(s[-1])

one_vote = summ / 450

dic = {}

for s in list_strings:
    dic[''.join(s[:-1])] = int(int(s[-1]) // one_vote)

if sum(dic.values()) < 450:
    list_ost = []
    for s in list_strings:
        name = ''.join(s[:-1])
        ost = int(s[-1]) % one_vote
        list_ost.append((name, ost))
    list_ost.sort(key=lambda x: x[1], reverse=True)
    for i in range(450 - int(sum(dic.values()))):
        dic[list_ost[i][0]] += 1

for s in list_strings:
    print(' '.join(s[:-1]), dic[''.join(s[:-1])])