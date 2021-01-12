import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))

dp = [1] * N
result = 0
for i in range(N):
    for x in range(0, i):
        if array[i] > array[x]:
            dp[i] = max(dp[i], dp[x] + 1)
    result = max(dp[i], result)

print(result)