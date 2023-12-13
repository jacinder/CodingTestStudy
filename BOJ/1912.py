n = int(input())
m = list( map(float, input().split(' ')))

for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i-1])

print(int(max(m)))
