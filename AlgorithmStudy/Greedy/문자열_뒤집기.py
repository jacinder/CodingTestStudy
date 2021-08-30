# https://www.acmicpc.net/problem/1439
S = input()
dummy = [0,0]
prev = -1

for curr in S:
	if curr != prev:
		dummy[int(curr)] += 1
	prev = curr

print(min(dummy))