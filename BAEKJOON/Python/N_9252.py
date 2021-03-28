import sys
input = sys.stdin.readline

str_1 = " " + input().replace('\n', '')
str_2 = " " + input().split('\n')[0]
len_1 = len(str_1)
len_2 = len(str_2)

dp = [["" for __ in range(len_2)] for _ in range(len_1)]

for x in range(1, len_1):
    for y in range(1, len_2):
        if str_1[x] == str_2[y]:
            dp[x][y] = dp[x - 1][y - 1] + str_1[x]
        else:
            dp[x][y] = max(dp[x - 1][y], dp[x][y - 1], key = lambda x : len(x))

print(len(dp[-1][-1]), dp[-1][-1], sep='\n')