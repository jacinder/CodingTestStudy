import sys
units = []
cnt, money = map(int, sys.stdin.readline().split())
for _ in range(cnt):
    units.append(int(sys.stdin.readline()))

dp = [2e9] * (money+1)
for cost in range(1, money+1):
    if cost in units:
        dp[cost] = 1
    else:
        for coin in units:
            if cost > coin:
                dp[cost] = min(dp[cost], dp[cost-coin]+1)

if dp[money] == 2e9:
    print(-1)
else:
    print(dp[money])
