import sys
input = sys.stdin.readline

N = int(input())
nowTab = list(map(int, input().split()))
realTab = list(map(int, input().split()))

result = 0
beforeDiff = 0
for x in range(N):
    different = nowTab[x] - realTab[x]

    if different >= 0:
        if beforeDiff < 0:
            result += abs(beforeDiff)
            beforeDiff = different
        elif different > beforeDiff:
            beforeDiff = different
        else:
            result += beforeDiff - different
            beforeDiff = different

    else:
        if beforeDiff > 0:
            result += beforeDiff
            beforeDiff = different
        elif different < beforeDiff:
            beforeDiff = different
        else:
            result += abs(beforeDiff - different)
            beforeDiff = different

result += abs(beforeDiff)
print(result)
