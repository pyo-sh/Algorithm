import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_heard = set(input()[:-1] for _ in range(N))
no_see = set(input()[:-1] for _ in range(M - 1))
no_see.add(input())

arr = sorted(list(no_heard & no_see))
print(len(arr))
for string in arr:
    print(string)