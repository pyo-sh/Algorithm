import sys
input = sys.stdin.readline

N = int(input())
ATM = list(map(int, input().split()))

ATM.sort()
result = 0
for i in range(N):
    result += (N - i) * ATM[i]
print(result)