def adventurer(N, gongpodo):
	group = 0
	count = 0
	# rest = []
	
	gongpodo.sort()
	print(gongpodo)
	for i in gongpodo:
		count += 1
		if i <= count:
			group += 1
			count = 0
	
	print(group)

adventurer(5, [2,3,1,2,2])