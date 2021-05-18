import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = sorted(list(map(int, input().split())))
visited = [False] * N

def dfs(stack, cnt):
    global N, M, array, visited
    if cnt >= M:
        print(*stack)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                stack[cnt] = array[i]
                dfs(stack, cnt + 1)
                visited[i] = False
    
dfs([0] * M, 0)