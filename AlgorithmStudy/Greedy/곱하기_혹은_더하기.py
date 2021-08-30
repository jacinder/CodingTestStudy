string = input()
result = 0
for num in string:
	if num == 0 or num == 1 or result == 0 or result == 1:
		result += int(num)
	else:
		result *= int(num)

print(result)