diction = {}
while True:
    try:
        a = input().split()
        if len(a) == 1:
            if a[0] not in diction.keys():
                diction[a[0]] = 1
            else:
                diction[a[0]] += 1
        else:
            for word in a:
                if word not in diction.keys():
                    diction[word] = 1
                else:
                    diction[word] += 1
    except EOFError:
        break

key_list = [(value, key) for key, value in diction.items()]
key_list.sort(key=lambda x: (-x[0], x[1]))
result = [x[1] for x in key_list]
for i in result:
    print(i)
