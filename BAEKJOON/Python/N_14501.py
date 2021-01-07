length = int(input())

work = [0] * length
for i in range(length):
    work[i] = list(map(int, input().split()))

dp = [0] * (length + 1)
for i in reversed(range(length)):
    workTime, workPay = work[i]
    if workTime <= length - i:
        dp[i] = max(dp[i + workTime] + workPay, dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])