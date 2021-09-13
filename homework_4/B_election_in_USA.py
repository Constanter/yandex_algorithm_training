box_dict = {}
while True:
	try:
		inp = input()
		key , value = inp.split()
		if key not in box_dict.keys():
			box_dict[key] = int(value)
		else:
			box_dict[key] += int(value)
	except EOFError:
		break

for i in sorted(box_dict.keys()) :
	print(i, box_dict[i])