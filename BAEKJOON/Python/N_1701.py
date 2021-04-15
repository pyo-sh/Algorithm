import sys
input = sys.stdin.readline

string = input().replace('\n', '')

result = 0

for i in range(len(string)):
    nowStr = string[i:]
    nowLength = len(nowStr)
    lps = [0] * nowLength

    y = 0
    maximum = 0
    for x in range(1, nowLength):
        while y > 0 and nowStr[x] != nowStr[y]:
            y = lps[y - 1]
        if nowStr[x] == nowStr[y]:
            y += 1
            lps[x] = y
            maximum = max(maximum, y)
    result = max(maximum, result)

print(result)