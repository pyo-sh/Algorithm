length = int(input())

dp = [0] * 3
for i in range(length):
    temp = [min(dp[1], dp[2]), min(dp[0], dp[2]), min(dp[0], dp[1])]
    house = list(map(int, input().split()))
    dp[0] = temp[0] + house[0]
    dp[1] = temp[1] + house[1]
    dp[2] = temp[2] + house[2]

print(min(dp))