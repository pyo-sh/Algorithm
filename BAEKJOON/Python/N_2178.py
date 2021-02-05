import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

history = [input() for _ in range(N)]
check = [[False] * M for _ in range(N)]

# 최소라서 BFS 로 풀어봄
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
queue = deque([(0, 0, 0)])
while queue:
  y, x, times = queue.popleft()
  if y == N - 1 and x == M - 1:
    print(times + 1)
    break
  
  if not check[y][x]:
    check[y][x] = True
    
    for i in range(4):
      dx = x + move[i][0]
      dy = y + move[i][1]
      if 0 <= dx < M and 0 <= dy < N:
        if history[dy][dx] == '1' and not check[dy][dx]:
          queue.append((dy, dx, times + 1))
