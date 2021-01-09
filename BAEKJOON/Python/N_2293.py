import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

dp = [0] * (K + 1)
# 자기 자신을 포함하는 것은 한 가지의 가능성
dp[0] = 1
for i in range(N):
    nowCoin = coin[i]
    for num in range(nowCoin, K + 1):
        if num - nowCoin >= 0:
            dp[num] += dp[num - nowCoin]

print(dp[K])