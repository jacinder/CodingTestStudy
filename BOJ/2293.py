import sys
cnt, money = map(int, sys.stdin.readline().split())
units = []

for _ in range(cnt):
    units.append(int(sys.stdin.readline()))

dp = [1] + [0]*(money)

for coin in units:
    for cost in range(1, money+1):
        if cost >= coin:
            dp[cost] += dp[cost-coin]

print(dp[money])
