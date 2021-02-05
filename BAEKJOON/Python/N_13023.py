import sys
input = sys.stdin.readline

N, M = map(int, input().split())

friends = [[] for _ in range(N)]
for m in range(M):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

result = 0
check = [False] * N
def DFS(node, depth):
  check[node] = True
  global result
  
  if depth >= 4:
    result = 1
  else:
    for x in friends[node]:
      if not check[x]:
        DFS(x, depth + 1)
  
  check[node] = False

for i in range(N):
  DFS(i, 0)
  if result == 1:
    break

print(result)