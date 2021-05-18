import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(arr, cnt):
    global N, M
    if cnt > M:
        print(*arr)
    else:
        start = arr[cnt - 2] + 1 if cnt != 1 else cnt
        for i in range(start, N + 1):
            arr[cnt - 1] = i
            dfs(arr, cnt + 1)
    
dfs([0] * M, 1)