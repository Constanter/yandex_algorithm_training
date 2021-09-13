num = int(input())
testimonies = []
for i in range(num):
    testimonies.append(input())

num = int(input())
plates = []
for i in range(num):
    plates.append(input())

length = []
counter = 0

for plate in plates:
    for testimony in testimonies:
        counter += 1
        temp_plate = [i for i in plate]
        for letter in set(testimony):
            if letter in temp_plate:
                temp_plate.remove(letter)
            else:
                counter -= 1
                break
    length.append(counter)
    counter = 0

max_res = max(length)
indexies = []
for i in range(len(length)):
    if max_res == length[i]:
        indexies.append(i)

for i in indexies:
    print(plates[i])