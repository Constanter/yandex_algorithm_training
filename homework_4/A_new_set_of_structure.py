box_count = int(input())

box_dict = {}
for i in range(box_count):
	key , value = map(int,input().split())
	if key not in box_dict.keys():
		box_dict[key] = value
	else:
		box_dict[key] += value

for i in sorted(box_dict.keys()):
	print(i, box_dict[i])